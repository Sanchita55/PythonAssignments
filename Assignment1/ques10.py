totalpop = 80000
popmen = totalpop*52/100
popwomen = totalpop - popmen
poplit = (totalpop*48)/100
litmen = (popmen*35)/100
litwomen = poplit - litmen
unlitmen = popmen - litmen
unlitwomen = popwomen - litwomen

print('Total Population : ',totalpop)
print('Total Men : ',popmen)
print('Total Women : ',popwomen)
print('Total Literacy : ',poplit)
print('Total Literate Men : ',litmen)
print('Total Literate Women: ',litwomen)
print('Total Illiterate Men: ',unlitmen)
print('Tota Illiterate Women: ',unlitwomen)