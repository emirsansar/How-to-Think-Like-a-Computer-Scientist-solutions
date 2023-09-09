import calendar

cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2022)                   # What happens here?

# cl 2012 takvimini yazdırıyor.

print(calendar.isleap(2000))  # artık yıl olup olmadığını kontrol ediyor.

d = calendar.LocaleTextCalendar(6, "SPANISH")       # ayları ispanyolca yazar
d.pryear(2012)

