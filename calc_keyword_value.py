#coding: utf8 
import re
import sys

rule_dict = {
	ur'海龙|鼎好|科贸|E世界|中关村|电子城':100,
	ur'(海龙|鼎好|科贸|E世界|中关村)\d+':150,
	ur'座|楼|层|室|地址|公司|房间':150,
	ur'\d{3:}':50,
	ur'奸商|JS':50,
	ur'曝光|证据':50,
	ur'上当|被骗|受骗|骗子|骗':100,
	ur'[ABC]':20,
	ur'黑店|被黑|宰|坑|强行|强迫|逼':80,
	ur'防骗|攻略|欺诈|折腾|倒霉|惨痛':30,
	ur'解决':10,
	ur'损失|亏':100,
	ur'元|大洋|块|千|万|价格':10,
	ur'电话|电脑|手机|单反|相机|笔记本|本|机器|数码':10,
	ur'报警|投诉|举报|求助':30,
	ur'攒机':10,
	ur'经历|经过':10,
	ur'忽悠|销售':10,
	ur'店':10,
	ur'价钱|价格|报价':10,
	ur'便宜':10,
	ur'提货|拿货|没货|换':10,
	ur'选|买':10,
	ur'交钱|发票':10,
	ur'商家|卖家':10,
	ur'型号|配置':10,
	ur'拿回|退':10,
	ur'员工':10,
	ur'死全家|TMD|麻痹|操你妈|草泥马':10,
	ur'导购':10,
	ur'年*月*日':10,
}

def calc_article_value (infile, rule=rule_dict, tempstring = ur'中关村鼎好101室奸商死全家，骗了我3千多块钱') :
	f = open(infile, "r")
	res = 0
	lines = f.read()
	lines = unicode(lines,"utf8")
	f.close()


	for key in rule:
		print key
		try:
			# m = re.search(key, tempstring)
			m = re.search(key, lines)
			if m:
				res += rule[key]
		except:
			print "key not valid : " + key
	return res

def get_file_length(infile):
	f = open(infile, "r")
	res = len(f.read())
	infile.close()
	return res
		
if __name__ == "__main__":
	value = calc_article_value(sys.argv[1])
	print value

