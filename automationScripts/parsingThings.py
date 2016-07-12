# coding=utf-8
def transformFunction(inputString):
    count = 0
    out = "["
    splitString = inputString.split(',')
    for item in splitString:
        count+=1
        aux = "(\'{0}\',\'{1}\')".format(count,item)
        out += aux
        if count < len(splitString):
            out += ","
    out += "]"
    return out

def transformForJSON(inputString):
    count = 0
    out = "{"
    splitString = inputString.split(',')
    for item in splitString:
        aux = "\'{0}\':".format(item)
        aux += "{"
        aux2 = "{0}".format(count)
        aux2 += "}"
        aux += aux2
        out += aux
        count+=1
        if count < len(splitString):
            out += ","
    out += "}"
    return out

def pseudoOneHotEncodingJSON(inputString, neighborhood):   
    count = 1
    out = "{"
    splitString = inputString.split(',')
    for item in splitString:
        aux = "\'{0}\':{1}".format(item,1) if count == neighborhood  else "\'{0}\':{1}".format(item,0)
        out += aux
        count+=1
        if count < len(splitString):
            out += ","
    out += "}"
    return out

#OLD 
#stringTransform = "review_scores_rating,reviews_per_month,number_of_reviews,first_review,last_review,street,zipcode,latitude,longitude,host_about,host_since,host_listings_count,host_identity_verified,calendar_updated,availability_30,availability_60,availability_90,availability_365,cancellation_policy,bathrooms,bedrooms,beds,accommodates,guests_included,extra_people,security_deposit"
#stringAmenities = "tv,internet,kitchen,ac,smoking,hottub,heating,family,events,dryer,smoke,shampoo,elevator,washer,intercom,essentials,lock,24hourcheckin,hangers,laptopf,hairdryer,iron,firstaidkit,cabletv,fireplace,extinguisher,breakfast,pets,petsallowed,parking,safetycard,doorman,wheelchair,carbondetector,gym,washerdryer,pool"
#stringVerifications ="verified_email,verified_phone,verified_facebook,verified_linkedin,verified_google,verified_jumio,verified_reviews,verified_manual"
#stringNeighborhoods = "baro_de_viver,can_baro,can_peguera,canyelles,ciutat_meridiana,diagonal_mar_i_el_front_maritim_del_poblenou,horta,hostafrancs,montbau,navas,pedralbes,porta,provencals_del_poblenou,sant_andreu,sant_antoni,sant_genis_dels_agudells,sant_gervasi_-_galvany,sant_gervasi_-_la_bonanova,sant_marti_de_provencals,sant_pere,_santa_caterina_i_la_ribera,sants,sants_-_badal,sarria,torre_baro,vallcarca_i_els_penitents,vallvidrera,_el_tibidabo_i_les_planes,verdun,vilapicina_i_la_torre_llobeta,el_baix_guinardo,el_barri_gotic,el_besos_i_el_maresme,el_bon_pastor,el_camp_d_en_grassot_i_gracia_nova,el_camp_de_l_arpa_del_clot,el_carmel,el_clot,el_coll,el_congres_i_els_indians,el_fort_pienc,el_guinardo,el_parc_i_la_llacuna_del_poblenou,el_poble_sec,el_poblenou,el_putxet_i_el_farro,el_raval,el_turo_de_la_peira,l_antiga_esquerra_de_l_eixample,la_barceloneta,la_bordeta,la_clota,la_dreta_de_l_eixample,la_font_d_en_fargues,la_font_de_la_guatlla,la_guineueta,la_marina_de_port,la_marina_del_prat_vermell,la_maternitat_i_sant_ramon,la_nova_esquerra_de_l_eixample,la_prosperitat,la_sagrada_familia,la_sagrera,la_salut,la_teixonera,la_trinitat_nova,la_trinitat_vella,la_vall_d_hebron,la_verneda_i_la_pau,la_vila_olimpica_del_poblenou,la_vila_de_gracia,les_corts,les_roquetes,les_tres_torres"
#stringtypeApp = "apartment,bed_&_breakfast,boat,bungalow,cabin,camper_rv,chalet,condominium,dorm,house,loft,other,tent,townhouse,villa,yurt"
#stringEntireAp = "entire_home_apt,private_room,shared_room"
#stringTypeBed = "airbed,couch,futon,pull-out_sofa,real_bed"

stringTransform = "street,zipcode,latitude,longitude,host_about,host_listings_count,host_identity_verified,availability_30,availability_60,availability_90,availability_365,cancellation_policy,bathrooms,bedrooms,beds,accommodates,guests_included,extra_people,security_deposit"
stringAmenities = "tv,internet,kitchen,ac,smoking,hottub,heating,family,events,dryer,smoke,shampoo,elevator,washer,intercom,essentials,lock,24hourcheckin,hangers,laptopf,hairdryer,iron,firstaidkit,cabletv,fireplace,extinguisher,breakfast,pets,petsallowed,parking,safetycard,doorman,wheelchair,carbondetector,gym,washerdryer,pool"
stringVerifications ="verified_email,verified_phone,verified_facebook,verified_linkedin,verified_google,verified_jumio,verified_reviews,verified_manual"
stringNeighborhoods = "baro_de_viver,can_baro,can_peguera,canyelles,ciutat_meridiana,diagonal_mar_i_el_front_maritim_del_poblenou,horta,hostafrancs,montbau,navas,pedralbes,porta,provencals_del_poblenou,sant_andreu,sant_antoni,sant_genis_dels_agudells,sant_gervasi_-_galvany,sant_gervasi_-_la_bonanova,sant_marti_de_provencals,sant_pere,_santa_caterina_i_la_ribera,sants,sants_-_badal,sarria,torre_baro,vallcarca_i_els_penitents,vallvidrera,_el_tibidabo_i_les_planes,verdun,vilapicina_i_la_torre_llobeta,el_baix_guinardo,el_barri_gotic,el_besos_i_el_maresme,el_bon_pastor,el_camp_d_en_grassot_i_gracia_nova,el_camp_de_l_arpa_del_clot,el_carmel,el_clot,el_coll,el_congres_i_els_indians,el_fort_pienc,el_guinardo,el_parc_i_la_llacuna_del_poblenou,el_poble_sec,el_poblenou,el_putxet_i_el_farro,el_raval,el_turo_de_la_peira,l_antiga_esquerra_de_l_eixample,la_barceloneta,la_bordeta,la_clota,la_dreta_de_l_eixample,la_font_d_en_fargues,la_font_de_la_guatlla,la_guineueta,la_marina_de_port,la_marina_del_prat_vermell,la_maternitat_i_sant_ramon,la_nova_esquerra_de_l_eixample,la_prosperitat,la_sagrada_familia,la_sagrera,la_salut,la_teixonera,la_trinitat_nova,la_trinitat_vella,la_vall_d_hebron,la_verneda_i_la_pau,la_vila_olimpica_del_poblenou,la_vila_de_gracia,les_corts,les_roquetes,les_tres_torres"
stringtypeApp = "apartment,bed_&_breakfast,boat,bungalow,cabin,camper_rv,chalet,condominium,dorm,house,loft,other,tent,townhouse,villa,yurt"
stringEntireAp = "entire_home_apt,private_room,shared_room"
stringTypeBed = "airbed,couch,futon,pull-out_sofa,real_bed"

print transformForJSON(stringTransform)
#print transformForJSON(stringTransform)
#print transformFunction(stringTransform)
