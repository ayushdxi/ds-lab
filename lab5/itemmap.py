import fileinput

for line in fileinput.input():
    data = line.strip().split(',')
    #SNo,ObservationDate,Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered
    if line.startswith('SNo'):
        continue
    if len(data) == 8:
        sno, observation_date, state, country, last_update, confirmed, deaths, recovered = data
        print('{0}, {1}'.format(country,confirmed))