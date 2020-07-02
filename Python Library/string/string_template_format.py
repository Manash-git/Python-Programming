from string import Template

text= 'The quick brown $animal $action over the $state $victim'

temp=Template(text)

print(temp.substitute(animal="Fox",action="jump",state='lazy',victim="Dog"))

sr = "Hello $country. This is $lang Code"

print(Template(sr).substitute(lang="Python",country="Bangladesh"))

area= "Rampura"
zip_code=1219

address= Template("$home, Dhaka - $post_code.")
print(address.substitute(home=area,post_code=zip_code))