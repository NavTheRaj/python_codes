
sec=int(input("Enter the time in seconds=>"));

hour=sec//(60*60)

rem_sec=sec%3600

mins=sec//60-hour*60

seconds=sec%60

print (hour,"Hour",mins,"Minute",seconds,"Seconds");
