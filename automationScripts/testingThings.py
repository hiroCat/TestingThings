# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 03:58:37 2016

@author: hiro
"""
form =['41.37698108','2.174762754',2,2,2,2,2,2,2]


def createJSONString(form):
    x = "'review_scores_rating':{0},'reviews_per_month':{1},'number_of_reviews':{2},'first_review':{3},'last_review':{4}," \
        "'street':{5},'zipcode':{6},'latitude':{7},'longitude':{8},'host_about':{9}," \
        "'host_since':{10},'host_listings_count':{11},'host_identity_verified':{12},'calendar_updated':{13},'availability_30':{14}," \
        "'availability_60':{15},'availability_90':{16},'availability_365':{17},'cancellation_policy':{18},'bathrooms':{19}," \
        "'bedrooms':{20},'beds':{21},'accommodates':{22},'guests_included':{23},'extra_people':{24}," \
        "'security_deposit':{25}"

    stringAmenities = "tv,internet,kitchen,ac,smoking,hottub,heating,family,events,dryer,smoke,shampoo,elevator,washer,intercom,essentials,lock,24hourcheckin,hangers,laptopf,hairdryer,iron,firstaidkit,cabletv,fireplace,extinguisher,breakfast,pets,petsallowed,parking,safetycard,doorman,wheelchair,carbondetector,gym,washerdryer,pool"
    stringVerifications ="verified_email,verified_phone,verified_facebook,verified_linkedin,verified_google,verified_jumio,verified_reviews,verified_manual"
    stringNeighborhoods = "baro_de_viver,can_baro,can_peguera,canyelles,ciutat_meridiana,diagonal_mar_i_el_front_maritim_del_poblenou,horta,hostafrancs,montbau,navas,pedralbes,porta,provencals_del_poblenou,sant_andreu,sant_antoni,sant_genis_dels_agudells,sant_gervasi_-_galvany,sant_gervasi_-_la_bonanova,sant_marti_de_provencals,sant_pere,_santa_caterina_i_la_ribera,sants,sants_-_badal,sarria,torre_baro,vallcarca_i_els_penitents,vallvidrera,_el_tibidabo_i_les_planes,verdun,vilapicina_i_la_torre_llobeta,el_baix_guinardo,el_barri_gotic,el_besos_i_el_maresme,el_bon_pastor,el_camp_d_en_grassot_i_gracia_nova,el_camp_de_l_arpa_del_clot,el_carmel,el_clot,el_coll,el_congres_i_els_indians,el_fort_pienc,el_guinardo,el_parc_i_la_llacuna_del_poblenou,el_poble_sec,el_poblenou,el_putxet_i_el_farro,el_raval,el_turo_de_la_peira,l_antiga_esquerra_de_l_eixample,la_barceloneta,la_bordeta,la_clota,la_dreta_de_l_eixample,la_font_d_en_fargues,la_font_de_la_guatlla,la_guineueta,la_marina_de_port,la_marina_del_prat_vermell,la_maternitat_i_sant_ramon,la_nova_esquerra_de_l_eixample,la_prosperitat,la_sagrada_familia,la_sagrera,la_salut,la_teixonera,la_trinitat_nova,la_trinitat_vella,la_vall_d_hebron,la_verneda_i_la_pau,la_vila_olimpica_del_poblenou,la_vila_de_gracia,les_corts,les_roquetes,les_tres_torres"
    stringtypeApp = "apartment,bed_&_breakfast,boat,bungalow,cabin,camper_rv,chalet,condominium,dorm,house,loft,other,tent,townhouse,villa,yurt"
    stringEntireAp = "entire_home_apt,private_room,shared_room"
    stringTypeBed = "airbed,couch,futon,pull-out_sofa,real_bed"

    x = x.format(0,0,0,0,0,0,0,form[0],form[1],0,0,0,0,0,0,0,0,0,form[2],form[3],form[4],form[5],form[6],form[7],form[8],0)
    print "nanan"
    xAmenities = pseudoOneHotEncodingJSONAmenities(stringAmenities,form.data['Amenities'])
    xVerification = pseudoOneHotEncodingJSONVerifications(stringVerifications,(form.data['verificationUser']-1))
    xNeighborhoods = pseudoOneHotEncodingJSON(stringNeighborhoods,(form.data['neighborhood']-1))
    xAppType = pseudoOneHotEncodingJSON(stringtypeApp,(form.data['apartamentType']-1))
    xEntireApp = pseudoOneHotEncodingJSON(stringEntireAp,(form.data['typeOfRoom']-1))
    xTypeBed = pseudoOneHotEncodingJSON(stringTypeBed,(form.data['typeOfBed']-1))
    return x + "," + xAmenities + "," + xVerification + "," + xNeighborhoods + "," + xAppType + "," + xEntireApp + "," + xTypeBed

def pseudoOneHotEncodingJSON(listItems, number):
    count = 0
    out = "{"
    splitString = listItems.split(',')
    for item in splitString:
        aux = "\'{0}\':{1}".format(item, 1) if count == number else "\'{0}\':{1}".format(item, 0)
        out += aux
        count += 1
        if count < len(splitString):
            out += ","
    out += "}"
    return out

def pseudoOneHotEncodingJSONVerifications(stringVerifications,verifications):
    count = 0
    out = "{"
    aux = ""
    splitString = stringVerifications.split(',')
    for item in splitString:
        for v in verifications:
            if ("verified_" + v.lower() == item):
                aux = "\'{0}\':{1}".format(item, 1)
                break;
            else:
                aux ="\'{0}\':{1}".format(item, 0)
        out += aux
        count += 1
        if count < len(splitString):
            out += ","
    out += "}"
    return out

def pseudoOneHotEncodingJSONAmenities(stringAmenities,amenities):
    count = 0
    out = "{"
    aux = ""
    splitString = stringAmenities.split(',')
    for item in splitString:
        for a in amenities:
            if (parseStringAm(a) == item):
                aux = "\'{0}\':{1}".format(item, 1)
                break;
            else:
                aux ="\'{0}\':{1}".format(item, 0)
        out += aux
        count += 1
        if count < len(splitString):
            out += ","
    out += "}"
    return out

def parseStringAm(a):
    a = a.lower()
    a = a.replace(" ","")
    a = a.replace("/","")
    if a == 'wirelessInternet':
        return 'internet'
    if a == 'airconditioning':
        return 'ac'
    if a == 'smokingallowed':
        return 'smoking'
    if a == 'familykidfriendly':
        return 'family'
    if a == 'suitableforevents':
        return 'events'
    if a == 'smokedetector':
        return 'smoke'
    if a == 'elevatorinbuilding':
        return 'elevator'
    if a == 'buzzerwirelessintercom':
        return 'intercom'
    if a == 'lockonbedroomdoor':
        return 'lock'
    if a == '24-hourcheck-in':
        return '24hourcheckin'
    if a == 'laptopfriendlyworkspace':
        return 'laptopf'
    if a == 'indoorfireplace':
        return 'fireplace'
    if a == 'fireextinguisher':
        return 'extinguisher'
    if a == 'petsliveonthisproperty' or a == 'otherpet(s)' or a == 'dog(s)' or a == 'cat(s)':
        return 'pets'
    if a == 'freeparkingonpremises':
        return 'parking'
    if a == 'wheelchairaccessible':
        return 'wheelchair'
    if a == 'carbonmonoxidedetector':
        return 'wheelchair'
    return a