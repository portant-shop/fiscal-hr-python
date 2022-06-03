from fiscalhr.fiscal import Fiscal

if __name__ == '__main__':
    fis = Fiscal('/home/vedran/projects/shop/fiskal_2.pem', '/home/vedran/projects/shop/fiskal_2.pem', key_passphrase='ABC123')

    now = fis.localtime_now()

    racun = fis.create('RacunType')
    racun.Oib = '01234567890'
    racun.USustPdv = True
    racun.DatVrijeme = fis.format_time(now)
    racun.OznSlijed = 'P'
    racun.BrRac.BrOznRac = 7
    racun.BrRac.OznPosPr = 'PP-1'
    racun.BrRac.OznNapUr = 'NAP-4'

    porez = fis.create('Porez')
    porez.Stopa = fis.format_decimal(25)
    porez.Osnovica = fis.format_decimal(100)
    porez.Iznos = fis.format_decimal(25)

    racun.Pdv = fis.create('PdvType')
    racun.Pdv.Porez.append(porez)

    racun.IznosUkupno = fis.format_decimal(125)
    racun.NacinPlac = 'K'
    racun.OibOper = '01234567890'
    racun.NakDost = False

    racun.ZastKod = fis.generate_zki(racun)

    print(racun.ZastKod)

    response = fis.send('racuni', racun)

    print(response)
