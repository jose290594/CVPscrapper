from bs4 import BeautifulSoup
import sys
import os
import urllib.request
import pylint

#variables#
                                        # websiteTarget=website to be scrapped
                                        #websiteData= raw website data
                                        #soupDump= dump of website data in a BeautifulSoup object
                                        #artclistDump= raw articles list data
                                        #artcList= raw articles names 
                                        #artcList2= list with clean articles names
                                        #artcLink= link from target article
                                        #artclinkList= list from all article's links
                                        #artclinklistDum= temp all article's links

                            
websiteTarget = str('https://www.nysenate.gov/legislation/laws/CVP')
websiteData = urllib.request.urlopen(websiteTarget).read().decode()
soupDump =  BeautifulSoup(websiteData, 'html.parser')
artclistDump = str(soupDump.find_all(class_='c-law-link-loc-id'))
soupDump2 = BeautifulSoup(artclistDump, 'html.parser')
artcList = soupDump2('a')
artcList2 = []
artcLink = None
artclinkList = []
artclinklistDum = []
sectList = []


for tag in artcList:
    dummyTrim=str((tag.get_text('a')))
    dummyTrim=dummyTrim.replace('\n                      ', '' )                    
    dummyTrim=dummyTrim.replace('                    ', '' )
    artcList2.append(dummyTrim)
    print(dummyTrim)
    dummyTrim=None

for tag in artcList:
    artclinkList.append(str('https://www.nysenate.gov')+str(tag.get('href')))
seclinklistDum = []
sectlinkSubl = []
sectList=[[] for x in range(len(artcList))]
secttitList=[[] for x in range(len(artcList))]
for x in range(0, int(len(artclinkList))):
    websitetargetDum=artclinkList[x]
    websitedataDum = urllib.request.urlopen(websitetargetDum).read().decode()
    soupdumpDum =  BeautifulSoup(websitedataDum, 'html.parser')
    artclistdumpDum = str(soupdumpDum.find_all(class_='c-law-link-loc-id'))
    secttitListDump = str(soupdumpDum.find_all(class_="c-law-link-title"))
    soupdumpDum2 = BeautifulSoup(artclistdumpDum, 'html.parser')
    soupDump3 = BeautifulSoup(secttitListDump, 'html.parser')
    artclistDum = soupdumpDum2('a')
    secttitListDum = soupDump3('a')
    
    #### por cada articulo en lista
    seclinklistDum = []
    for tag in artclistDum:
            dummyTrim=tag.get_text('a')
            dummyTrim=dummyTrim.replace('\n                      ', '' )                    
            dummyTrim=dummyTrim.replace('                    ', '' )
            sectList[x].append(dummyTrim)
            seclinklistDum.append(str('https://www.nysenate.gov')+str(tag.get('href')))
            print(dummyTrim)
    sectlinkSubl.append(seclinklistDum)
    for tag in secttitListDum:
            dummyTrim=tag.get_text('a')
            dummyTrim=dummyTrim.replace('\n                      ', '' )                    
            dummyTrim=dummyTrim.replace('                      ', '' )
            secttitList[x].append(dummyTrim)
            print(dummyTrim)
        
    
    secttitList.append(seclinklistDum)
sectContent = [[] for x in range(len(sectlinkSubl))]
for y in range(0, int(len(sectlinkSubl))):
    for yyy in range(0, int(len(sectlinkSubl[y]))):
        websitetargetDum2=sectlinkSubl[y][yyy]
        print(websitetargetDum2)
        websitedataDum2 = urllib.request.urlopen(websitetargetDum2).read().decode()
        soupdumpDum4 =  BeautifulSoup(websitedataDum2, 'html.parser')
        sectcontentdumpDum = str(soupdumpDum4.find_all(class_="c-law-doc-text"))
        soupdumpDum5 = BeautifulSoup(sectcontentdumpDum, 'html.parser')
        artclistDum2 = soupdumpDum5('div')
        print(artclistDum2)
        for tag in artclistDum2:
            dummyTrim=tag.get_text('div')

            sectContent[y].append(dummyTrim)
            
print(sectContent)


print(sectList)    


print(secttitList)
    
for z in range(len(artcList)):
    dumpfile= open("final.txt", "a+")
    dumpfile.write(str(artcList[z])+"\n"+"\n"+'\n')
    for zz in range(len(sectList[z])):
        dumpfile.write(str(sectList[z][zz])+': '+str(secttitList[z][zz])+'\n'+str(sectContent[zz])+'\n'+'\n')
    dumpfile.close()