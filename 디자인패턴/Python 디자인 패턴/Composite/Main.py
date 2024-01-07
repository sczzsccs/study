from Folder import*

root = Folder(name="root")
root.add(unit=File(name="a.txt", size=1000))
root.add(unit=File(name="b.txt", size=2000))

sub1 = Folder(name="sub1")
sub1.add(unit=File(name="sa.txt", size=100))
sub1.add(unit=File(name="sa.txt", size=4000))
root.add(unit=sub1)

sub2 = Folder(name="sub2")
sub2.add(unit=File(name="sa.txt", size=250))
sub2.add(unit=File(name="sb.txt", size=340))
root.add(unit=sub2)

root.List()