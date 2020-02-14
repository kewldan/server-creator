from PyQt5 import QtWidgets, QtCore, QtGui
from ui import Ui_Form
import sys
from PyQt5.QtGui import QIcon
import rc_rc

#Form initialization
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()
def toXML(xml):
    if xml == "Creative island":
        return "data/tiles/island12.xml"
def check(button):
    return str(button.isChecked()).lower()

def confirm():
    name=ui.name.text()
    try:
        port=int(ui.port.text())
        ui.port_1.setText("Port:")
    except ValueError:
        ui.port_1.setText("Port: (ERR)")
        return
    port=str(port)
    players=str(ui.players.value())
    password=ui.password.text()
    island=ui.island.currentText()
    ad=check(ui.ad_mode)
    dn=ui.dn_l.value()
    sunrise=str(ui.sunrise.value()/100)
    sunset=str(ui.sunset.value()/100)
    stock=check(ui.stock)
    al=check(ui.all)
    menu=check(ui.menu)
    fp=check(ui.first_per)
    fpv=check(ui.fir_per_veh)
    vd=check(ui.damage_veh)
    pd=check(ui.player_damage)
    npc=check(ui.npc_damage)
    sharks=check(ui.sharks)
    megalodon=check(ui.megalodon)
    tpv=check(ui.tp_veh)
    ft=check(ui.fast_travels)
    fuel=check(ui.fuel)
    starting=str(ui.starting.value())
    unlock=check(ui.un_comp)
    saved=open("server_config.xml","w")
    code='''
<?xml version="1.0" encoding="UTF-8"?>
<server_data port="{}" name="{}" seed="31164" save_name="" max_players="{}" password="{}" advanced_mode="{}" day_night_length="{}" sunrise="{}" sunset="{}" infinite_stock="{}" unlock_all_islands="{}" creative_menu="{}" base_island="{}" first_person="{}" first_person_vehicle="{}" vehicle_damage="{}" player_damage="{}" npc_damage="{}" sharks="{}" megalodon="{}" teleport_vehicle="{}" fast_travel="{}" limited_fuel="{}" starting_currency="{}" unlock_components="{}">
	<admins>
		<id value="76561198080294966"/>
	</admins>
	<blacklist/>
	<whitelist/>
	<playlists>
		<path value="rom/data/missions/arctic_mining"/>
		<path value="rom/data/missions/arctic_search_and_rescue"/>
		<path value="rom/data/missions/arctic_survey"/>
		<path value="rom/data/missions/brilliant_fuels_oil"/>
		<path value="rom/data/missions/clam_oil_company"/>
		<path value="rom/data/missions/default_elevators"/>
		<path value="rom/data/missions/default_fluid_gantries"/>
		<path value="rom/data/missions/default_fuel_stores"/>
		<path value="rom/data/missions/fishing_community"/>
		<path value="rom/data/missions/lighthouse"/>
		<path value="rom/data/missions/long_distance_shipping"/>
		<path value="rom/data/missions/mega_island"/>
		<path value="rom/data/missions/research_center"/>
		<path value="rom/data/missions/sea_fort_tours"/>
		<path value="rom/data/missions/skye_power_company"/>
	</playlists>
</server_data>
    '''.format(port,name,players,password,ad,dn,sunrise,sunset,stock,al,menu,toXML(island),fp,fpv,vd,pd,npc,sharks,megalodon,tpv,ft,fuel,starting,unlock)
    saved.write(code)


    
    

ui.confirm.clicked.connect(lambda: confirm() )
def changeValue(value,type2,obj):
    if type2 == "players":
        a="Max players: "
    if type2 == "sunrise":
        a="Sunrise: "
    if type2 == "sunset":
        a="Sunset: "
    if type2 == "start":
        a="Starting currency: "
    if type2 == "DN":
        a="Day and night length: "
    obj.setText(a+str(value))
ui.players.valueChanged[int].connect(lambda: changeValue(ui.players.value(),"players",ui.play))
ui.sunrise.valueChanged[int].connect(lambda: changeValue(ui.sunrise.value()/100,"sunrise",ui.sunrise_1))
ui.sunset.valueChanged[int].connect(lambda: changeValue(ui.sunset.value()/100,"sunset",ui.sunset_1))
ui.starting.valueChanged[int].connect(lambda: changeValue(ui.starting.value(),"start",ui.start_1))
ui.dn_l.valueChanged[int].connect(lambda: changeValue(ui.dn_l.value(),"DN",ui.dn_l_1))







sys.exit(app.exec_())