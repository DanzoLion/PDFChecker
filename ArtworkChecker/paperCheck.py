def sizeCheck(readPDF):

    n = int()
    for i in readPDF.pages:
                    n = n + 1
                    print('\n')
                    print(f'\rPage No.: {n}')

                    floatArtBoxW = str(i.artbox.width)
                    floatArtBoxH = str(i.artbox.height)
                    floatAWidth = float(floatArtBoxW)/72*25.4
                    floatAHeight = float(floatArtBoxH)/72*25.4
                    #print(f'Artbox Dimensions: {floatAWidth}W and {floatAHeight}H')
                    # print(f'Artbox Dimensions: {floatArtBoxW}W and {floatArtBoxH}H')
                    print(50*'-')
                    
                    floatTrimW = str(i.trimbox.width) 
                    floatTrimH = str(i.trimbox.height)
                    floatTWidth = float(floatTrimW)/72*25.4
                    floatTHeight = float(floatTrimH)/72*25.4 
                    print(f'The PDF WIDTH is: {round(floatTWidth)}mm')
                    print(f'The PDF HEIGHT is: {round(floatTHeight)}mm')
                    floatBleedW = str(i.bleedbox.width)
                    floatBleedH = str(i.bleedbox.height)
                    floatBWidth = float(floatBleedW)/72*25.4
                    floatBHeight = float(floatBleedH)/72*25.4 
                    print(f'The BLEED WIDTH is: {(round(floatBWidth))}mm')
                    print(f'The BLEED HEIGHT is: {(round(floatBHeight))}mm')
                   
                    overallBeed = abs(round(floatTWidth-floatBWidth))/2
                    print(f'Overall Bleed: {overallBeed}mm')
                    bleedFromEdge = abs(round(floatTWidth-floatBWidth))/2
                    print(f'Page Bleed from each Edge: {bleedFromEdge}mm')
               
                    if round(floatTWidth) == 52 and round(floatTHeight) ==74:
                        print('Your Page Size is A8 Portrait')
                    elif    round(floatTWidth) == 74 and round(floatTHeight) ==105: 
                        print('Your Page Size is A7 Portrait')
                    elif   round(floatTWidth) == 105 and round(floatTHeight) ==148:
                        print('Your Page Size is A6 Portrait')
                    elif    round(floatTWidth) == 148 and round(floatTHeight) ==210:
                        print('Your Page Size is A5 Portrait')
                    elif    round(floatTWidth) == 210 and round(floatTHeight) ==297:
                        print('Your Page Size is A4 Portrait')
                    elif    round(floatTWidth) == 297 and round(floatTHeight) ==420:
                        print('Your Page Size is A3 Portrait')
                    elif    round(floatTWidth) == 420 and round(floatTHeight) ==594: 
                        print('Your Page Size is A2 Portrait')
                    elif     round(floatTWidth) == 594 and round(floatTHeight) ==841:
                        print('Your Page Size is A1 Portrait')
                    elif    round(floatTWidth) == 841 and round(floatTHeight) ==1189:
                        print('Your Page Size is A0 Portrait')
                    
                    elif round(floatTWidth) == 74 and round(floatTHeight) ==52:
                        print('Your Page Size is A8 Landscape')
                    elif    round(floatTWidth) == 105 and round(floatTHeight) ==74: 
                        print('Your Page Size is A7 Landscape')
                    elif   round(floatTWidth) == 148 and round(floatTHeight) ==105:
                        print('Your Page Size is A6 Landscapre')
                    elif    round(floatTWidth) == 210 and round(floatTHeight) ==148:
                        print('Your Page Size is A5 Landscape')
                    elif    round(floatTWidth) == 297 and round(floatTHeight) ==210:
                        print('Your Page Size is A4 Landscape')
                    elif    round(floatTWidth) == 420 and round(floatTHeight) ==297:
                        print('Your Page Size is A3 Landscape')
                    elif    round(floatTWidth) == 594 and round(floatTHeight) ==420: 
                        print('Your Page Size is A2 Landscape')
                    elif     round(floatTWidth) == 841 and round(floatTHeight) ==420:
                        print('Your Page Size is A1 Landscape')
                    elif    round(floatTWidth) == 1189 and round(floatTHeight) ==841:
                        print('Your Page Size is A0 Landscape')
                    
                    elif    round(floatTWidth) == 210 and round(floatTHeight) ==99:
                        print('Your Page Size is DL Landscape')
                    elif    round(floatTWidth) == 99 and round(floatTHeight) ==210:
                        print('Your Page Size is DL Portrait')

                    elif    round(floatTWidth) == 210 and round(floatTHeight) ==210:
                        print('Your Page Size is 210mm Square')
                    elif    round(floatTWidth) == 148 and round(floatTHeight) ==148:
                        print('Your Page Size is 148mm Square')
                    elif    round(floatTWidth) == 105 and round(floatTHeight) ==105:
                        print('Your Page Size is 105mm Square')
                    
                    elif    round(floatTWidth) == 85 and round(floatTHeight) ==55:
                        print('Your Page Size is European Business Card Landscape')
                    elif    round(floatTWidth) == 55 and round(floatTHeight) ==85:
                        print('Your Page Size is European Business Card Portrait')
                    
                    
                    elif print(f'**WARNING!** Your Page is not  standard size.  Please check your product matches the page size uploaded '):
                        pass

                    if n == 2:
                        print(f'\nThanks, check your {n} page document, if more than 2 pages, we will send an artwork proof')
                        break

                    if overallBeed == 0:
                        print(f'**WARNING!** Your PDF has no bleed')
                        print(f'Do you want to continue?')
  
    return print(f'End of Artwork Check')
