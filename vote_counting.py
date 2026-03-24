# Contagem dos votos

vb = int(input('Quantos votos brancos tiveram?: '))
vn = int(input('Quantos votos nulos tiveram?: '))
vv = int(input('Quantos votos válidos tiveram?: '))

vf = ( vb + vn + vv)
vbp = (100 * vb ) / vf
vnp = (100 * vn ) / vf
vvp = (100 * vv ) / vf

print(f'A porcentagem dos votos foram: {vbp} brancos, {vnp}, nulos e {vvp} válidos')
