#Python Program that checks the amount of days between two dates

import datetime

OriginalDateYear = input("Please enter the original date year: ");
OriginalDateMonth = input("Please enter the original date month: ");
OriginalDateDay = input("Please enter the original date day: ");

OriginalDate = datetime.date(int(OriginalDateYear),int(OriginalDateMonth),int(OriginalDateDay));

print("Original Date : " + str(OriginalDate));

newDateYear = input("Please enter the new date year: ");
newDateMonth = input("Please enter the new date month: ");
newDateDay = input("Please enter the new date day: ");

newDate = datetime.date(int(newDateYear),int(newDateMonth),int(newDateDay));

print("New Date : " + str(newDate));
DifferenceDates = newDate - OriginalDate;
print("The dates are " + str(DifferenceDates.days) + " day(s) apart");
