from subprocess import PIPE, run
import requests


if __name__ == "__main__":
    thread_template = '''
    In 2018 i started logging every time i masturbate. I eventually wrote a script to time me and automatically add entries. This is the content of my fap.log as of 8th May 2022
    
    Time format is 24 hour time
    Duration format is hours/minutes/seconds
    "timed" faps are those which have recorded the duration using my fap_logger script
    "untimed" faps are those which i have added with my fap_logger script but have not been timed (no duration)
    durations/times with ?? in them means i'm not sure what the time/duration was
    
    [SPOILER="fap.json"]
    this has gotten too large for UC to handle. 
    [url]%GHOSTBIN_URL%[/url]
    [/SPOILER]
    
    
    [SPOILER="More human-readable version"]
    [CODE]
    %HUMAN_READABLE%
    [/CODE]
    [/SPOILER]
    
    
    
    I also wrote a couple of scripts to add up all the times and give me stats
    
    output of duration.py
    [CODE]
    %DURATION_OUTPUT%
    [/CODE]
    
    output of stats.py
    [CODE]
    %STATS_OUTPUT%
    [/CODE]
    
    I don't know if i'm genuinely retarded or something but i don't really see a problem with this :^)
    '''
    
    
    with open("fap.json", "r") as f:
        fap_log_content = f.read()
    
    paste_response = requests.post("https://pst.klgrth.io/paste/new", data={
        "lang":"text", 
        "text":fap_log_content,
        "expire":"-1",
        "password":"",
        "title":"fap.log by guylet @ unknowncheats.me"},
        allow_redirects=True)
    
    if paste_response.status_code != 200:
        print(f"Error creating ghostbin paste. Status code = {paste_response.status_code}")
        exit()
    
    stats_output = run(["python", "stats.py"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    duration_ouput = run(["python", "duration.py"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    human_output = run(["python", "human-readable.py"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    thread_template = thread_template.replace("%DURATION_OUTPUT%", duration_ouput.stdout.rstrip("\n"))
    thread_template = thread_template.replace("%STATS_OUTPUT%", stats_output.stdout.rstrip("\n"))
    thread_template = thread_template.replace("%HUMAN_READABLE%", human_output.stdout.rstrip("\n"))
    thread_template = thread_template.replace("%GHOSTBIN_URL%", paste_response.url)
    
    print(thread_template)
