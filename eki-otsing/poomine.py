#!/usr/bin/python
# -*- coding: utf-8 -*-

# Poomismängu- ja ristsõnalahendaja
# Kasutab EKI andmebaasi
# Märge tulevikuks: ära kasuta re-d html-i töötlemiseks! BeautifulSoup!
# A. Roots 2010

import urllib, re, sys, StringIO


def main(input, program_mode=0):
    global otsitav, tulemused, ei_sobi, global_source
    
    tulemused = []
    ei_sobi = ''
    global_source = StringIO.StringIO()
    otsitav = ''
    
    otsitav = input
    
    save_source()
    search_results()
    
    # Poomismängus tuleb kõrvaldada korduvad tähed
    if program_mode:
        eliminate_impossible()
    
    kuvatavad_vastused = '| '
    for vastus in tulemused:
        # Väldime duplikaate
        if vastus.upper() in kuvatavad_vastused.upper():
            pass
        else:
            kuvatavad_vastused = kuvatavad_vastused + vastus.upper() + ' | '
    
    # Tagasta tuple
    return len(tulemused), kuvatavad_vastused


# Otsib etteantud reast vastet    
def search_line(line):
    global tulemused
    expression = '(<font color="red">(.*?)</font>|<span style="font-weight:bold;">(.*?)</span>)'
    match = re.compile(expression).search(line)
        
    if match:
        # EKI-s on vastused erinevas formaadis, korjame üleliigse ära
        puhastatud_vastus = remove_html_tags(match.group(1))
        tulemused.append(puhastatud_vastus)
                

# Avab source faili ja söödab sealt rida-rea kaupa andmeid
def search_results():
    
    global_source.seek(0)
    line = global_source.readline()
    while line:
        # Mõni vastus on teisite formaaditud, eemalda see
        if 'background-color:lightsalmon;' in line:
            search_line(line.replace('background-color:lightsalmon;',''))
        else:
            search_line(line)
        line = global_source.readline()
    global_source.close()
    

# Haara eki source koos vastustega ja salvesta faili
def save_source():
    global otsitav, global_source
    otsitav_safe = urllib.urlencode({'Q':otsitav})
    eki_url = 'http://www.eki.ee/dict/qs2006/index.cgi?'+otsitav_safe+'&F=M&O=0&E=0'
    fd = urllib.urlopen(eki_url)
    global_source.write(fd.read())
    
    

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# Poomismängu puhul võta võimatud sõnad välja
def eliminate_impossible():
    global tulemused, otsitav, ei_sobi
    
    otsi_man = []
    for letter in otsitav:
        otsi_man.append(letter)
    
    #Iga EKI sõnaga tee...    
    for tulemus in tulemused:
        letterman = []
        missing_char = []
        
        #Iga tähega selles sõnas tee...
        for tulemus_letter in tulemus:
            letterman.append(tulemus_letter)
        
        if len(letterman) <= len(otsi_man):
            #Nüüd on sõna kõik tähed letterman-is
            cnt = 0
            for l in letterman:
                if l == otsi_man[cnt]:
                    pass
                else:
                    missing_char.append(l)
                cnt += 1
            aa = set(missing_char)
            bb = set(otsitav)
            if set(aa) & set (bb):
                ei_sobi = ei_sobi +' '+ tulemus
                tulemused.remove(tulemus)
