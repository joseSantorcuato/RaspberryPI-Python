#Taller e&m

from string import Template

distros = Template("Una de las principales distros linux es $name, bienvenido!")
print distros.substitute(name="Ubuntu")
print distros.substitute(name="Debian")
print distros.substitute(name="REHT")
