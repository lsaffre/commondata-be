# -*- coding: UTF-8 -*-
# Copyright 2014 Luc Saffre
# License: BSD (see file COPYING for details)
from __future__ import unicode_literals




def populate(pg):

    pg.set_args('fr nl de en')
    pg.province("Liège", "Luik", "Lüttich", "Liège")
    pg.set_args('zip_code fr nl de en')

    pg.city("4000", "Liège", "Luik", "Lüttich", "Liège")
    pg.township("4000", "Glain", "", "")
    pg.township("4000", "Rocourt", "", "")
    pg.township("4020", "Bressoux", "", "")
    pg.township("4020", "Jupille-sur-Meuse", "", "")
    pg.township("4020", "Wandre", "", "")
    pg.township("4030", "Grivegnée", "", "", wa="Grimgnêye")
    pg.township("4031", "Angleur", "", "")
    pg.township("4032", "Chênée", "", "")
    
    pg.city("4750", "Butgenbach", "Butgenbach", "Bütgenbach", "Butgenbach")
    pg.city("4760", "Bullange", "Büllingen", "Büllingen", "Büllingen")
    pg.city("4780", "Saint-Vith", "Sankt Vith", "Sankt Vith", "Sankt Vith")
    pg.city("4780", "Recht", "Recht", "Recht", "Recht")
    pg.city("4837", "Baelen", "Baelen", "Baelen", "Baelen")

    pg.city("4040", "Herstal", "", "", "")
    pg.township("4041", "Milmort", "", "", wa="Mérmwète")
    pg.township("4041", "Vottem", "", "", "")
    pg.city("4042", "Liers", "", "", "")
    pg.city("4050", "Chaudfontaine", "", "", "")
    pg.city("4051", "Vaux-sous-Chèvremont", "", "", "")
    pg.city("4052", "Beaufays", "", "", "")
    pg.city("4053", "Embourg", "", "", "")
    pg.city("4100", "Boncelles", "", "", "")
    pg.city("4100", "Seraing", "", "", "")
    pg.city("4101", "Jemeppe-sur-Meuse", "", "", "")
    pg.city("4102", "Ougrée", "", "", "")
    pg.city("4120", "Neupré", "", "", "")
    pg.township("4120", "Rotheux-Rimière", "", "", "")
    pg.township("4120", "Ehein (Neupré)", "", "", "")
    pg.township("4121", "Neuville-en-Condroz", "", "", "")
    pg.township("4122", "Plainevaux", "", "", "")
    pg.village("4120", "Houte-Si-Plou", "", "", "")
    
    pg.city("4130", "Esneux", "", "", "")
    pg.city("4130", "Tilff", "", "", "")
    pg.city("4140", "Dolembreux", "", "", "")
    pg.city("4140", "Gomze-Andoumont", "", "", "")
    pg.city("4140", "Rouvreux", "", "", "")
    pg.city("4140", "Sprimont", "", "", "")
    pg.city("4141", "Louveigné (Sprimont)", "", "", "")
    pg.city("4160", "Anthisnes", "", "", "")
    pg.city("4161", "Villers-aux-Tours", "", "", "")
    pg.city("4162", "Hody", "", "", "")
    pg.city("4163", "Tavier", "", "", "")
    pg.city("4170", "Comblain-au-Pont", "", "", "")
    pg.city("4171", "Poulseur", "", "", "")
    pg.city("4180", "Comblain-Fairon", "", "", "")
    pg.city("4180", "Comblain-la-Tour", "", "", "")
    pg.city("4180", "Hamoir", "", "", "")
    pg.city("4181", "Filot", "", "", "")
    pg.city("4190", "Ferrières", "", "", "")
    pg.city("4190", "My", "", "", "")
    pg.city("4190", "Vieuxville", "", "", "")
    pg.city("4190", "Werbomont", "", "", "")
    pg.city("4190", "Xhoris", "", "", "")
    pg.city("4210", "Burdinne", "", "", "")
    pg.city("4210", "Hannêche", "", "", "")
    pg.city("4210", "Lamontzée", "", "", "")
    pg.city("4210", "Marneffe", "", "", "")
    pg.city("4210", "Oteppe", "", "", "")
    pg.city("4217", "Héron", "", "", "")
    pg.city("4217", "Lavoir", "", "", "")
    pg.city("4217", "Waret-l'Evêque", "", "", "")
    pg.city("4218", "Couthuin", "", "", "")
    pg.city("4219", "Acosse", "", "", "")
    pg.city("4219", "Ambresin", "", "", "")
    pg.city("4219", "Meeffe", "", "", "")
    pg.city("4219", "Wasseiges", "", "", "")
    pg.city("4250", "Boëlhe", "", "", "")
    pg.city("4250", "Geer", "", "", "")
    pg.city("4250", "Hollogne-sur-Geer", "", "", "")
    pg.city("4250", "Lens-Saint-Servais", "", "", "")
    pg.city("4252", "Omal", "", "", "")
    pg.city("4253", "Darion", "", "", "")
    pg.city("4254", "Ligney", "", "", "")
    pg.city("4257", "Berloz", "", "", "")
    pg.city("4257", "Corswarem", "", "", "")
    pg.city("4257", "Rosoux-Crenwick", "", "", "")
    pg.city("4260", "Avennes", "", "", "")
    pg.city("4260", "Braives", "", "", "")
    pg.city("4260", "Ciplet", "", "", "")
    pg.city("4260", "Fallais", "", "", "")
    pg.city("4260", "Fumal", "", "", "")
    pg.city("4260", "Ville-en-Hesbaye", "", "", "")
    pg.city("4261", "Latinne", "", "", "")
    pg.city("4263", "Tourinne (Lg.)", "", "", "")
    pg.city("4280", "Abolens", "", "", "")
    pg.city("4280", "Avernas-le-Bauduin", "", "", "")
    pg.city("4280", "Avin", "", "", "")
    pg.city("4280", "Bertrée", "", "", "")
    pg.city("4280", "Blehen", "", "", "")
    pg.city("4280", "Cras-Avernas", "", "", "")
    pg.city("4280", "Crehen", "", "", "")
    pg.city("4280", "Grand-Hallet", "", "", "")
    pg.city("4280", "Lens-Saint-Remy", "", "", "")
    pg.city("4280", "Merdorp", "", "", "")
    pg.city("4280", "Moxhe", "", "", "")
    pg.city("4280", "Petit-Hallet", "", "", "")
    pg.city("4280", "Poucet", "", "", "")
    pg.city("4280", "Thisnes", "", "", "")
    pg.city("4280", "Trognée", "", "", "")
    pg.city("4280", "Villers-le-Peuplier", "", "", "")
    pg.city("4280", "Wansin", "", "", "")
    pg.city("4280", "Hannut", "Hannuit", "Hannut", "Hannut")
    pg.city("4287", "Pellaines", "", "", "")
    pg.city("4287", "Racour", "", "", "")
    pg.city("4287", "Lincent", "Lijsem", "Lincent", "Lincent")
    pg.city("4300", "Bettincourt", "", "", "")
    pg.city("4300", "Bleret", "", "", "")
    pg.city("4300", "Bovenistier", "", "", "")
    pg.city("4300", "Grand-Axhe", "", "", "")
    pg.city("4300", "Lantremange", "", "", "")
    pg.city("4300", "Oleye", "", "", "")
    pg.city("4300", "Waremme", "", "", "")
    pg.city("4317", "Aineffe", "", "", "")
    pg.city("4317", "Borlez", "", "", "")
    pg.city("4317", "Celles (Lg.)", "", "", "")
    pg.city("4317", "Faimes", "", "", "")
    pg.city("4317", "Les Waleffes", "", "", "")
    pg.city("4317", "Viemme", "", "", "")
    pg.city("4340", "Awans", "", "", "")
    pg.city("4340", "Fooz", "", "", "")
    pg.city("4340", "Othée", "", "", "")
    pg.city("4340", "Villers-l'Evêque", "", "", "")
    pg.city("4342", "Hognoul", "", "", "")
    pg.city("4347", "Fexhe-le-Haut-Clocher", "", "", "")
    pg.city("4347", "Freloux", "", "", "")
    pg.city("4347", "Noville (Lg.)", "", "", "")
    pg.city("4347", "Roloux", "", "", "")
    pg.city("4347", "Voroux-Goreux", "", "", "")
    pg.city("4350", "Lamine", "", "", "")
    pg.city("4350", "Momalle", "", "", "")
    pg.city("4350", "Pousset", "", "", "")
    pg.city("4350", "Remicourt", "", "", "")
    pg.city("4351", "Hodeige", "", "", "")
    pg.city("4357", "Donceel", "", "", "")
    pg.city("4357", "Haneffe", "", "", "")
    pg.city("4357", "Jeneffe (Lg.)", "", "", "")
    pg.city("4357", "Limont", "", "", "")
    pg.city("4360", "Bergilers", "", "", "")
    pg.city("4360", "Grandville", "", "", "")
    pg.city("4360", "Lens-sur-Geer", "", "", "")
    pg.city("4360", "Otrange", "", "", "")
    pg.city("4360", "Oreye", "Oerle", "Oreye", "Oreye")
    pg.city("4367", "Crisnée", "", "", "")
    pg.city("4367", "Fize-le-Marsal", "", "", "")
    pg.city("4367", "Kemexhe", "", "", "")
    pg.city("4367", "Odeur", "", "", "")
    pg.city("4367", "Thys", "", "", "")
    pg.city("4400", "Awirs", "", "", "")
    pg.city("4400", "Chokier", "", "", "")
    pg.city("4400", "Flémalle", "", "", "")
    pg.city("4400", "Flémalle-Grande", "", "", "")
    pg.city("4400", "Flémalle-Haute", "", "", "")
    pg.city("4400", "Gleixhe", "", "", "")
    pg.city("4400", "Ivoz-Ramet", "", "", "")
    pg.city("4400", "Mons-lez-Liège", "", "", "")
    pg.city("4420", "Montegnée", "", "", "")
    pg.city("4420", "Saint-Nicolas (Lg.)", "", "", "")
    pg.city("4420", "Tilleur", "", "", "")
    pg.city("4430", "Ans", "", "", "")
    pg.city("4431", "Loncin", "", "", "")
    pg.city("4432", "Alleur", "", "", "")
    pg.city("4432", "Xhendremael", "", "", "")
    pg.city("4450", "Juprelle", "", "", "")
    pg.city("4450", "Lantin", "", "", "")
    pg.city("4450", "Slins", "", "", "")
    pg.city("4451", "Voroux-lez-Liers", "", "", "")
    pg.city("4452", "Paifve", "", "", "")
    pg.city("4452", "Wihogne", "", "", "")
    pg.city("4453", "Villers-Saint-Siméon", "", "", "")
    pg.city("4458", "Fexhe-Slins", "", "", "")
    pg.city("4460", "Bierset", "", "", "")
    pg.city("4460", "Grâce-Berleur", "", "", "")
    pg.city("4460", "Grâce-Hollogne", "", "", "")
    pg.city("4460", "Hollogne-aux-Pierres", "", "", "")
    pg.city("4460", "Horion-Hozémont", "", "", "")
    pg.city("4460", "Velroux", "", "", "")
    pg.city("4470", "Saint-Georges-sur-Meuse", "", "", "")
    pg.city("4480", "Clermont-sous-Huy", "", "", "")
    pg.city("4480", "Ehein (Engis)", "", "", "")
    pg.city("4480", "Engis", "", "", "")
    pg.city("4480", "Hermalle-sous-Huy", "", "", "")
    pg.city("4500", "Ben-Ahin", "", "", "")
    pg.city("4500", "Tihange", "", "", "")
    pg.city("4500", "Huy", "Hoei", "Huy", "Huy")
    pg.city("4520", "Antheit", "", "", "")
    pg.city("4520", "Bas-Oha", "", "", "")
    pg.city("4520", "Huccorgne", "", "", "")
    pg.city("4520", "Moha", "", "", "")
    pg.city("4520", "Vinalmont", "", "", "")
    pg.city("4520", "Wanze", "", "", "")
    pg.city("4530", "Fize-Fontaine", "", "", "")
    pg.city("4530", "Vaux-et-Borset", "", "", "")
    pg.city("4530", "Vieux-Waleffe", "", "", "")
    pg.city("4530", "Villers-le-Bouillet", "", "", "")
    pg.city("4530", "Warnant-Dreye", "", "", "")
    pg.city("4537", "Chapon-Seraing", "", "", "")
    pg.city("4537", "Seraing-le-Château", "", "", "")
    pg.city("4537", "Verlaine", "", "", "")
    pg.city("4540", "Amay", "", "", "")
    pg.city("4540", "Ampsin", "", "", "")
    pg.city("4540", "Flône", "", "", "")
    pg.city("4540", "Jehay", "", "", "")
    pg.city("4540", "Ombret", "", "", "")
    pg.city("4550", "Nandrin", "", "", "")
    pg.city("4550", "Saint-Séverin", "", "", "")
    pg.city("4550", "Villers-le-Temple", "", "", "")
    pg.city("4550", "Yernée-Fraineux", "", "", "")
    pg.city("4557", "Abée", "", "", "")
    pg.city("4557", "Fraiture", "", "", "")
    pg.city("4557", "Ramelot", "", "", "")
    pg.city("4557", "Seny", "", "", "")
    pg.city("4557", "Soheit-Tinlot", "", "", "")
    pg.city("4557", "Tinlot", "", "", "")
    pg.city("4560", "Bois-et-Borsu", "", "", "")
    pg.city("4560", "Clavier", "", "", "")
    pg.city("4560", "Les Avins", "", "", "")
    pg.city("4560", "Ocquier", "", "", "")
    pg.city("4560", "Pailhe", "", "", "")
    pg.city("4560", "Terwagne", "", "", "")
    pg.city("4570", "Marchin", "", "", "")
    pg.city("4570", "Vyle-et-Tharoul", "", "", "")
    pg.city("4577", "Modave", "", "", "")
    pg.city("4577", "Outrelouxhe", "", "", "")
    pg.city("4577", "Strée-lez-Huy", "", "", "")
    pg.city("4577", "Vierset-Barse", "", "", "")
    pg.city("4590", "Ellemelle", "", "", "")
    pg.city("4590", "Ouffet", "", "", "")
    pg.city("4590", "Warzée", "", "", "")
    pg.city("4600", "Lanaye", "", "", "")
    pg.city("4600", "Lixhe", "", "", "")
    pg.city("4600", "Richelle", "", "", "")
    pg.city("4600", "Visé", "", "", "")
    pg.city("4601", "Argenteau", "", "", "")
    pg.city("4602", "Cheratte", "", "", "")
    pg.city("4606", "Saint-André", "", "", "")
    pg.city("4607", "Berneau", "", "", "")
    pg.city("4607", "Bombaye", "", "", "")
    pg.city("4607", "Dalhem", "", "", "")
    pg.city("4607", "Feneur", "", "", "")
    pg.city("4607", "Mortroux", "", "", "")
    pg.city("4608", "Neufchâteau (Lg.)", "", "", "")
    pg.city("4608", "Warsage", "", "", "")
    pg.city("4610", "Bellaire", "", "", "")
    pg.city("4610", "Beyne-Heusay", "", "", "")
    pg.city("4610", "Queue-du-Bois", "", "", "")
    pg.city("4620", "Fléron", "", "", "")
    pg.city("4621", "Retinne", "", "", "")
    pg.city("4623", "Magnée", "", "", "")
    pg.city("4624", "Romsée", "", "", "")
    pg.city("4630", "Ayeneux", "", "", "")
    pg.city("4630", "Micheroux", "", "", "")
    pg.city("4630", "Soumagne", "", "", "")
    pg.city("4630", "Tignée", "", "", "")
    pg.city("4631", "Evegnée", "", "", "")
    pg.city("4632", "Cerexhe-Heuseux", "", "", "")
    pg.city("4633", "Melen", "", "", "")
    pg.city("4650", "Chaineux", "", "", "")
    pg.city("4650", "Grand-Rechain", "", "", "")
    pg.city("4650", "Herve", "", "", "")
    pg.city("4650", "Julémont", "", "", "")
    pg.city("4651", "Battice", "", "", "")
    pg.city("4652", "Xhendelesse", "", "", "")
    pg.city("4653", "Bolland", "", "", "")
    pg.city("4654", "Charneux", "", "", "")
    pg.city("4670", "Blégny", "", "", "")
    pg.city("4670", "Trembleur", "", "", "")
    pg.city("4670", "Mortier", "", "", "")
    pg.city("4671", "Barchon", "", "", "")
    pg.city("4671", "Housse", "", "", "")
    pg.city("4671", "Saive", "", "", "")
    pg.city("4672", "Saint-Remy (Lg.)", "", "", "")
    pg.city("4680", "Hermée", "", "", "")
    pg.city("4680", "Oupeye", "", "", "")
    pg.city("4681", "Hermalle-sous-Argenteau", "", "", "")
    pg.city("4682", "Heure-le-Romain", "", "", "")
    pg.city("4682", "Houtain-Saint-Siméon", "", "", "")
    pg.city("4683", "Vivegnis", "", "", "")
    pg.city("4684", "Haccourt", "", "", "")
    pg.city("4690", "Bassenge", "", "", "")
    pg.city("4690", "Boirs", "", "", "")
    pg.city("4690", "Eben-Emael", "", "", "")
    pg.city("4690", "Glons", "", "", "")
    pg.city("4690", "Roclenge-sur-Geer", "", "", "")
    pg.city("4690", "Wonck", "", "", "")
    pg.city("4700", "Eupen", "", "", "")
    pg.township("", "Nispert", "", "", "")
    pg.village("4701", "Kettenis", "", "", "")
    pg.city("4710", "Lontzen", "", "", "")
    pg.city("4711", "Walhorn", "", "", "")
    pg.city("4720", "La Calamine", "", "Kelmis")
    pg.city("4721", "Neu-Moresnet", "", "", "")
    pg.city("4728", "Hergenrath", "", "", "")
    pg.village("4730", "Raeren", "", "", "")
    pg.city("4730", "Hauset", "", "", "")
    pg.city("4731", "Eynatten", "", "", "")
    pg.city("4750", "Elsenborn", "", "", "")
    pg.city("4760", "Manderfeld", "", "", "")
    pg.city("4761", "Rocherath", "", "", "")
    pg.city("4770", "Amblève", "Amel", "Amel", "Amel")
    pg.village("4770", "Born", "", "", "")
    pg.village("4770", "Deidenberg", "", "", "")
    pg.village("4770", "Eibertingen", "", "", "")
    pg.village("4770", "Halenfeld", "", "", "")
    pg.village("4771", "Heppenbach", "", "", "")
    pg.village("4771", "Hepscheid", "", "", "")
    pg.village("4771", "Herresbach", "", "", "")
    pg.village("4771", "Iveldingen", "", "", "")
    pg.village("4771", "Medell", "", "", "")
    pg.village("4770", "Meyerode", "", "", "")
    pg.village("4771", "Mirfeld", "", "", "")
    pg.village("4771", "Möderscheid", "", "", "")
    pg.village("4771", "Montenau", "", "", "")
    pg.village("4771", "Schoppen", "", "", "")
    pg.village("4771", "Valender", "", "", "")
    pg.village("4771", "Wallerode", "", "", "")
    pg.village("4771", "Wereth", "", "", "")
    pg.city("4782", "Schoenberg", "", "Schönberg", "")
    pg.city("4783", "Lommersweiler", "", "", "")
    pg.city("4784", "Crombach", "", "", "")
    pg.city("4790", "Burg-Reuland", "", "", "")
    
    villages_in_reuland = """
    Aldringen
    Alster
    Auel
    Bracht
    Braunlauf
    Diepert
    Dürler
    Espeler
    Grüfflingen
    Koller
    Lascheid
    Lengeler
    Maldingen
    Maspelt
    Malscheid
    Oberhausen
    Oudler
    Ouren
    Richtenberg
    Steffeshausen
    Stoubach
    Thommen
    Weisten
    Weidig
    Weweler
    """
    for name in villages_in_reuland.strip().split():
        pg.village("4790", name, "", "", "")
    
    pg.city("4800", "Ensival", "", "", "")
    pg.city("4800", "Lambermont", "", "", "")
    pg.city("4800", "Petit-Rechain", "", "", "")
    pg.city("4800", "Polleur (Verviers)", "", "", "")
    pg.city("4800", "Verviers", "", "", "")
    pg.city("4801", "Stembert", "", "", "")
    pg.city("4802", "Heusy", "", "", "")
    pg.city("4820", "Dison", "", "", "")
    pg.city("4821", "Andrimont", "", "", "")
    pg.city("4830", "Limbourg", "", "", "")
    pg.city("4831", "Bilstain", "", "", "")
    pg.city("4834", "Goé", "", "", "")
    pg.city("4837", "Membach", "", "", "")
    pg.city("4840", "Welkenraedt", "", "", "")
    pg.city("4841", "Henri-Chapelle", "", "", "")
    pg.city("4845", "Jalhay", "", "", "")
    pg.city("4845", "Sart-lez-Spa", "", "", "")
    pg.city("4850", "Montzen", "", "", "")
    pg.city("4850", "Moresnet", "", "", "")
    pg.city("4850", "Plombières", "", "", "")
    pg.city("4851", "Gemmenich", "", "", "")
    pg.city("4851", "Sippenaeken", "", "", "")
    pg.city("4852", "Hombourg", "", "", "")
    pg.city("4860", "Cornesse", "", "", "")
    pg.city("4860", "Pepinster", "", "", "")
    pg.city("4860", "Wegnez", "", "", "")
    pg.city("4861", "Soiron", "", "", "")
    pg.city("4870", "Forêt", "", "", "")
    pg.city("4870", "Fraipont", "", "", "")
    pg.city("4870", "Nessonvaux", "", "", "")
    pg.city("4870", "Trooz", "", "", "")
    pg.city("4877", "Olne", "", "", "")
    pg.city("4880", "Aubel", "", "", "")
    pg.city("4890", "Clermont (Lg.)", "", "", "")
    pg.city("4890", "Thimister", "", "", "")
    pg.city("4890", "Thimister-Clermont", "", "", "")
    pg.city("4900", "Spa", "", "", "")
    pg.city("4910", "La Reid", "", "", "")
    pg.city("4910", "Polleur (Theux)", "", "", "")
    pg.city("4910", "Theux", "", "", "")
    pg.city("4920", "Aywaille", "", "", "")
    pg.city("4920", "Ernonheid", "", "", "")
    pg.city("4920", "Harzé", "", "", "")
    pg.city("4920", "Louveigné (Aywaille)", "", "", "")
    pg.city("4920", "Sougné-Remouchamps", "", "", "")
    pg.city("4950", "Faymonville", "", "", "")
    pg.city("4950", "Robertville", "", "", "")
    pg.city("4950", "Sourbrodt", "", "", "")
    pg.city("4950", "Waimes", "", "", "")
    pg.city("4950", "Weismes", "", "", "")
    pg.city("4960", "Bellevaux-Ligneuville", "", "", "")
    pg.city("4960", "Bevercé", "", "", "")
    pg.city("4960", "Malmédy", "", "", "")
    pg.city("4970", "Francorchamps", "", "", "")
    pg.city("4970", "Stavelot", "", "", "")
    pg.city("4980", "Fosse (Lg.)", "", "", "")
    pg.city("4980", "Trois-Ponts", "", "", "")
    pg.city("4980", "Wanne", "", "", "")
    pg.city("4983", "Basse-Bodeux", "", "", "")
    pg.city("4987", "Chevron", "", "", "")
    pg.city("4987", "La Gleize", "", "", "")
    pg.city("4987", "Lorcé", "", "", "")
    pg.city("4987", "Rahier", "", "", "")
    pg.city("4987", "Stoumont", "", "", "")
    pg.city("4990", "Arbrefontaine", "", "", "")
    pg.city("4990", "Bra", "", "", "")
    pg.city("4990", "Lierneux", "", "", "")
