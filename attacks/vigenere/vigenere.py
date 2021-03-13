################ INSPIRED BY ################
#   https://github.com/AndyStabler/Crypto   #
#############################################



import sys, os.path as path
import re

sys.path.insert(1, path.abspath(path.join('caesar')))
from caesar import count_chars, calculate_all_shifts



LOWER_BOUND = 0.060
UPPER_BOUND = 0.070

# calculate the IC value of 's'
def calculate_ic(s):
    N = len(s)
    F = count_chars(s)
    
    fsum = 0.0
    for i in range(26):
        fi = F[i];

        if (fi > 1.0):
            fsum += (fi * (fi - 1.0))
        
    return fsum / (N * (N - 1))

# guess the key length
def key_length(ct):
    l = len(ct)
    
    for k in range(2, l//2 + 1):
        sum = 0
        for i in range(k):
            s = ct[i::k]
            ic = calculate_ic(s)
            sum += ic
        average_ic = sum / k
        
        print("Average IC :", average_ic, "for key length =",k)
        
        if (average_ic >= LOWER_BOUND and average_ic <= UPPER_BOUND):
            return k

    return -1

# calculate the key
def find_key(keylen, ct):
    shifts = [0] * keylen
    
    for l in range(keylen):
        s = ct[l::keylen]
        shifts[l] = calculate_all_shifts(s)[0][0]
        
    return ''.join([chr(i + ord('A')) for i in shifts])
  
# decrypt 'ct' using 'key'
def decrypt(key, ct):
    l = len(key)
    plaintext = ''
    
    i = 0
    for c in ct:
        if not c.isalpha():
            plaintext += c
            continue
        
        v = (ord(c) - ord(key[i % l])) % 26
        plaintext += chr(v + 65)
        i += 1
        
    return plaintext


ct = "Cjwbfsbjnw ptpnihuzsubl (qi njuzqu pyl eiwemcojfjua) zq rkmxltaecgfn mvil wyykvq dg iaasa gyf (kpmvmefnverjar fmdfnrf) bcnl; cvw ulvxrrt, tbl gsy cwsjxv. Gcum wvrycgl wvnflvcsjn kstq th \"ucib\" bthpwrugktya ifwtqyzu rq ias jsxcf qw rwxwz kjwhtzrn, lc if tvikfsh icqfy is ckrpvy qk yi qgmcahd uwybbfj ddk gwdacai kft ifwtqyz. Vyc hxqcjnnl qw rlh-ymq hllrkmvkoxzd xrrvlsl cv efnugdyibqid vorukgdgg qf f qna kfpm gqflfr-mvw rkmxltaecgfn zsvwwuynp bdxg vgy, uaf tmcoszkjfl nzlzl qzqunnprjnlwa lt qvfvp bthpwrugktya ksawflpj zl p gse ofs. Nupkbxhzah mpjvktl ozw iyfkxltw ozgzhq vyc (rhbrwhnhtvb) sbtnahoyvp mu lctnnht xrpxhia efnugdyibqid ulbdccbl. Wn ss czrimkxr idliekkfb vov tj zbweb ih gwday gjv nghptwr, nuge rwx ggkyyz kj uttymfjx. Sqi cmtaxdj, nug jcrnfqld is vyc Sbtnaj–Brnckpg ymq jrpjrlvx gkzjgr fvntgra gs nug uguywkmqnl qw apeqcdfnvpx rwx rqkhlrvv jdzozaybz. Ke 1983, Bdg Qwhuyeudgia twmsx n hrqixf esd nb hzls wwauwygg cmvtfqlmgf (ke atkhias aeqlnh), tbl lmyegsw gxecawcai tpnihwywucjvph mc ckj fntxcg zfwmum (bt uguyszwsn gagch ht ojtocu). IQP'l gmuzlvvp btisvvx (ca rrpi) ndwf ybr fzdubqcdys bh zlixumj kupvfpxsobath — n dicpdhpjtotj zl utqbgwcai nmjer qeuupv kft lskmwcga fd GLO. Qf 1980, thr efsaw tiuyie c uguywkmqn 50-qkxgi giutjl nv rl tqdmfxy bh 1012 vjtfsvlfll efkenhmj tjrtrrxhba. Td 1984 nug jrpms wx ybr cir xg tiuyiekee peuwjnnuoj fpw olnfhpgu rd t dwasn jjvpt t 75-rqynn awdztk qwmqx og wyrmczwi ca 1012 qgcgthqgsm. Nfmycvsa as wbogsibbo ljwupfjdzm idxi zgrli mvil ybr qgcgthqgsm pqljs us xwwzbtdcs fikz kufvvp, ihc. Ugtlr'u cyl ifmvnwgu kfpm qweuoggi qexslk bcyn tmcmwvmj nb keagxoaw. Kupvfpxgu bwhbakhstl aiq hiavzljx hw vt mb cj utez, jmy qvnc kdlh tapyya ucexbl gs gnvycbthquff vpjgvah ifi wegrrxowbq, syvvycg ht eznwu jrq tosz tjya ularxgaxzfya gptwwklfvyg. 150-ugvbh vmrvrtj mu mvm cnhq qeat ngmv nh EUR fpos jwjh sctrdksl. Lmy rhwmgm kik llrckcg mvif fvbxv, zjm kik sig wepttgwffvyg fl utgb etxrte adfdcljlf. Dp rwx gbswn bh kft 21lh kwsnhtp, 150-bxzwb fzgogiq lxfm ft fbpxcg vcvknxrtvb p eozyj yaqlew dsg kntr hfp GLO. Vmrvrtj uxmv awayecc fjgrzwi xvizrh pszw xnvnc adggqvjlrf kmd aozv yi sctrdk wv 2005, lmihiy ktmvwvx qvnc nghpitqs pqerxgim lt czrimkx cdww nvov, ptjiqjnht mvw hbnm lt ergg npvs wj tnugi ktmvwvx mhey yh xztaunve tsgos kjdjgqxppivg lt vr wjcs. Tbwlmye fzqibbomnmukee uxobmwy bh rqnfamlwcp utftfsa ax nuck, scewsw fngctih hb aqrgrvigr vfghyifajrtfg, ifd weagrpgotqxcf jrq ias whuievllxmm bg ruxg lqt ht sftqyguet zoqfjx stfk ias xmgfve bcn."

ct = ct.upper()
replaced_ct = re.sub('[^a-zA-Z]+', '', ct).upper()

keylen = key_length(replaced_ct)

if keylen < 0:
    print("\nCould not find any key length! Exiting...")
    sys.exit()

key = find_key(keylen, replaced_ct)
pt = decrypt(key, ct)

print("\n" + "-" * 10 + " Potential results " + "-" * 10)
print("Key length :", keylen)
print("Key :", key)
print("Plaintext :", pt)
print("-" * 39)