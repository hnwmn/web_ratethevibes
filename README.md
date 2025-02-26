# Rate the Vibes - IntakeCTF 2024

**This was my challenge submission for IntakeCTF 2024.**  

## Category: Web

## Description

The society has set up a website to gather feedback to improve future events and competitions. Due to a misconfiguration, you may find a way to access more information than intended.

## Flag: 
Intake24{U1RBVFVTXzIwMF9PSw}

## Solution:

The first step is to discover the `/submissions` endpoint, which can be found either through the comment on the homepage that leads participants to `/submissions/archive` or by using a tool like Gobuster to find it directly. 

The description of the challenge should give enough understanding that the aim is to bypass the 403 forbidden message and get access to all user feedback. Researching should provide a bunch of methods for bypass. A common technique is to try different HTTP methods such as GET, POST, PUT, etc. If a POST request is sent to `/submissions`, participants get a hint to think about the request's origin. 

The correct method to bypass the 403 error is setting the `X-Forwarded-For` header to `127.0.0.1`. This simulates a misconfigured environment where requests originating from localhost are trusted and can bypass access controls. 

The following command can be used to retrieve the flag: `curl -H "X-Forwarded-For: 127.0.0.1" http://{ip}:{port}/submissions`, or manually set the header using a tool like Burp Suite and send the request.

## Previous Challenge: N/A
