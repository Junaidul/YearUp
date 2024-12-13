/*jslint browser:true */
"use strict";

function addMonths(elem) {
    let annualUseKw=0, dailyUseKw=0, i=0, x=0;
    let months=document.getElementById(elem).getElementsByTagName('input');


    for(i=0; i<months.length; i++) {
        x = Number(months[i].value);
        annualUseKw += x;
    }
    dailyUseKw = annualUseKw/365;
    return dailyUseKw;
}


function sunHours() {
    let hrs;
    let theZone = document.forms.solarForm.zone.selectedIndex;
    theZone +=1;
    switch(theZone) {
        case 1:
            hrs = 6;
            break;
        case 2:
            hrs = 5.5;
            break;
        case 3:
            hrs = 5;
            break;
        case 4:
            hrs = 4.5;
            break;
        case 5:
            hrs: 4.2;
            break;
        case 6:
            hrs = 3.5;
            break;
        default:
            hrs = 0;
    }
    return hrs;
}


function calculatePanel() {
    let userChoice = document.forms.solarForm.panel.selectedIndex;
    let panelOptions = document.forms.solarForm.panel.options;
    let power = panelOptions[userChoice].value;
    let name = panelOptions[userChoice].text;
    let x = [power, name];
    return x;
}


function calculateSolar() {
    let dailyUseKw = addMonths('mpc');
    //console.log(dailyUseKw);

    let sunHoursPerDay = sunHours();
    //console.log(sunHoursPerDay);

    let minKwNeeds = dailyUseKw/sunHoursPerDay;
    //console.log(minKwNeeds);

    let realKwNeeds = minKwNeeds * 1.25;
    //console.log(realKwNeeds);

    let realWattNeeds = realKwNeeds * 1000;
    //console.log(realWattNeeds);

    let panelInfo = calculatePanel();
    let panelOutput = panelInfo[0];
    let panelName = panelInfo[1];
    //console.log(panelOutput);
    //console.log(panelName);

    let panelsNeeded = Math.ceil(realWattNeeds / panelOutput);
    //console.log(panelsNeeded);

    let feedback = "";
    feedback += "<p>Based on your average daily use of "+ Math.round(dailyUseKw) +" kWh, you will need to purchase "+ panelsNeeded +" "+ panelName +" solar panels to offset 100% of you electricity bill.</p>";
    feedback += "<h2>Additional Details</h2>";
    feedback += "<p>Your average daily electricity consuption: "+ Math.round(dailyUseKw) +" Kwh per day.</p>";
    feedback += "<p>Average sunshine hours per day: "+ sunHoursPerDay +" hours</p>";
    feedback += "<p>Realisitic watts needed per hour: "+ Math.round(realWattNeeds) +" watts/hour.</p>";
    feedback += "<p>The "+ panelName +" panel you selected generates about "+ panelOutput +" watts per hour.</p>";

    document.getElementById('feedback').innerHTML = feedback;
}
message.txt
function downloadReport() {
    let feedbackContent = document.getElementById('feedback').innerText;
    let blob = new Blob([feedbackContent], { type: 'text/plain' });
    let link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = 'Solar_Calculator_Report.txt';
    link.click();
}