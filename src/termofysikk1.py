def opg_530():
    #a)
    M_tot = 1260 * 10**18 # kg
    percent_ocean = 0.965

    HC_fresh = 4168 # kg J / K
    HC_ocean = 3850 

    M_ocean = M_tot * percent_ocean
    M_fresh = M_tot * (1 - percent_ocean)


    print(f'Energi krevd for å varme opp havene: {M_ocean*HC_ocean} J')
    print(f'Energi krevd for å varme opp ferskvann: {M_fresh*HC_fresh} J')

    #b)
    forbruk = 147*10**9 #Wh
    hours = 24*365.25
    print(f'Norges forbruk i året: {forbruk*hours} J')
    print(f'Norges forbruk/energi krevd for å varme opp havene en grad: {forbruk*hours/(M_ocean*HC_ocean)}')

def opg_534():
    v = 200 #L
    A = 25 #m**2
    effekt_per_mm = 700 #W/m**2
    effektivitet = 0.4 #kun 40% av energien fanget går til oppvarmin
    effekt = A*effekt_per_mm*effektivitet
    print(f'Effekt er: {effekt} W')

    SHC_water = 4168 # kg J / K
    delta_t = 50-20 #Celsius ~ Kelvin

    energi_tot = v*SHC_water*delta_t #kg vann * kg J/K * K
    print(f'Total energi påkrevd: {energi_tot} J')
    print(f'Tid påkrevd: {energi_tot/effekt} sekunder, {energi_tot/effekt/60**2:.2f} timer')

opg_534()