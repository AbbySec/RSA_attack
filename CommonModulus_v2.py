#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,gmpy,base64
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def pad_even(x):#重要！凑齐2位，将0x1 变成 0x01
        return ('', '0')[len(x)%2] + x


def CipherB2n(c):#将base64编码后的密文转成数字
    c2 = base64.b64decode(c)
    temp = ''
    for i in c2:
        #temp += pad_even(str(hex(ord(i)))[2:])
        temp += pad_even(str(hex(i))[2:])
    temp = eval('0x'+temp)
    return (temp)

def CipherN2b(m):#将数字转换成ascii
    hex_m=hex(m)[2:]
    if hex_m[-1] == 'L' :
        hex_m=hex_m[:-1]
    return hex_m.decode('hex')

if __name__ == '__main__':
    
    sys.setrecursionlimit(1000000)
    e1 = 2064502724322065619610920801703770332444544578216378001086293531541437374183762889883952350512303123079541900923236233763161664622129759456230282585413446407867738585722011359806614520232070965281852076618382612714679676252453566235434477739937086238884216665488842132820363214479571428652601988484224495946375721070361900809019329649759575762397833605938043186770042654743067422241477268365617031178172027178755693566409032818917422094610812754447975895865178682453225583191912212367134587486285799782155109152944427348690163315056825740636659649124179137271843769782829849167189203185398850604993866726625112631363 #根据分解结果
    e2 = 345876628472173658667827209598382151105659756356047916616789608178750837186397400300720629651340906876883086914495035331197886605204006436370260001522881159036935864943407229927853909159622840262574082310844414506912374854901914383942533751831444966354228432405145711811352973922639155549967535687324229764372344162085165004285404573177532292355481437060424009838888577080364530392886743183323043816768429349194326761737705660684396204279082233532281958218079492085884478114686098035666343747253331397342623111000982654071759143224287261895337445430397635372322031624510827582994475842436489318181834008077000862716 #根据分解结果
    s = egcd(e1, e2)
    s1 = s[1]
    s2 = s[2]
    #c1 = '599595716443335281998311836057824471423872949240946858680326885165189798248960569757894506358411805849585756670489287378663084704040194999917555981780947347168038953586881042265439088817588061113649282685562685793490922993153055756402440331270258091628957614506114564171089877371669425927413409680720072212671386711718210703493452595971294376452211824154369667228880216368587635945779792347579255888106682362545743068441745513171129264302343262741956564684731698919731241320987319631379148776964502682709221865993042999911089876791270600102273290388573803610119258785910206047147140049692741145838272637793573255535'
    #c2 ='2770835070150439572361533458323853323331135769889806688952647723143090100332051468165048542378394448963218541675902047035925067679296545656936804088767980103951194340741696655103629403946052706547893699470917118074151642535282745768975138916426158727962237119890937352175934340987683034250582715361270008618676286594711314192182238464819951042936453477966710596316628687230956133831756510575129966303624319409792343130059271611653561066928057558199354900277398160189613164209414757242894166135226111274887275728717755076389566803028116652956415673871044558606548743531525162718902734213942283806624617372725072274578'
    #c1 = CipherB2n(c1)
    #c2 = CipherB2n(c2)
    c1 = 599595716443335281998311836057824471423872949240946858680326885165189798248960569757894506358411805849585756670489287378663084704040194999917555981780947347168038953586881042265439088817588061113649282685562685793490922993153055756402440331270258091628957614506114564171089877371669425927413409680720072212671386711718210703493452595971294376452211824154369667228880216368587635945779792347579255888106682362545743068441745513171129264302343262741956564684731698919731241320987319631379148776964502682709221865993042999911089876791270600102273290388573803610119258785910206047147140049692741145838272637793573255535
    c2 = 2770835070150439572361533458323853323331135769889806688952647723143090100332051468165048542378394448963218541675902047035925067679296545656936804088767980103951194340741696655103629403946052706547893699470917118074151642535282745768975138916426158727962237119890937352175934340987683034250582715361270008618676286594711314192182238464819951042936453477966710596316628687230956133831756510575129966303624319409792343130059271611653561066928057558199354900277398160189613164209414757242894166135226111274887275728717755076389566803028116652956415673871044558606548743531525162718902734213942283806624617372725072274578
    #print hex(c1)
    n = 2969137743448355327270876080101054338540503259878959630250143995627090090022850067465952425419364381562376747694180021046125245916815600955902349704778606351768446238203395142552910659278295524811626878015858630283055801066768074106075626751467085779562898859072146739523803688429510424565270597342059874774779917771627069956148632281761919668380478984737940333079018716867146763647145975313498463972109605022440637990931976478053161446536228883589512353452610817258565587291176075341583042418338206367482892585691607496654425794359814148329857831356779761901706016990032962092873983791585459395968897828575512138547 #共n
    if s1<0:
        s1 = - s1
        c1 = modinv(c1, n)
    elif s2<0:
        s2 = - s2
        c2 = modinv(c2, n)
    m=(pow(c1,s1,n)*pow(c2,s2,n)) % n
    print (m)
    #print (CipherN2b(m))