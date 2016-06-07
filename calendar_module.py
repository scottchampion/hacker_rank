import calendar

Weekdays = {0:"MONDAY",
			1:"TUESDAY",
			2:"WEDNESDAY",
			3:"THURSDAY",
			4:"FRIDAY",
			5:"SATURDAY",
			6:"SUNDAY"}

Month, Day, Year = map(int, raw_input().split())

print Weekdays[calendar.weekday(Year, Month, Day)]

