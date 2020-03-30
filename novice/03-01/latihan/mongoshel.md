
##berpindah ke db latihan jika db latihan sudah ada, jika belum maka db latihan akan dibuat dan langsung berpindah ke db latihan

>use latihan
```
switched to db latihan
```

##menampilkan db yang diakses
>db
```
latihan
```
##menampilkan semua db, jika ada database yang belum berisi data maka tidak akan di tampilkan
>show dbs
```
admin          0.000GB
config         0.000GB
local          0.000GB
myNewDatabase  0.000GB
```
>use latihan
```
switched to db latihan
```
##memasukan satu data dalam tabel list
>db.list.insert({"1":"user1"})
```
WriteResult({ "nInserted" : 1 })
```
>show dbs
```
admin          0.000GB
config         0.000GB
latihan        0.000GB
local          0.000GB
myNewDatabase  0.000GB
```
##memasukan banyak data sekaligus kedalam tabel 
> db.data.insertMany([
>... {user:"user1", name:"watashi", status:"admin"},
>... {user:"user2", name:"omaetachi", status:"guest"}
>... ])
```
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("5e818d555b72b98071a78813"),
		ObjectId("5e818d555b72b98071a78814")
	]
}
```
##menampilkan semua data yang terdapat pada tabel "data"
> db.data.find({})
```
{ "_id" : ObjectId("5e818d555b72b98071a78813"), "user" : "user1", "name" : "watashi", "status" : "admin" }
{ "_id" : ObjectId("5e818d555b72b98071a78814"), "user" : "user2", "name" : "omaetachi", "status" : "guest" }
```
##menampilkan data dengan tampilan yang mudah di pahami
> db.data.find({}).pretty()
```
{
	"_id" : ObjectId("5e818d555b72b98071a78813"),
	"user" : "user1",
	"name" : "watashi",
	"status" : "admin"
}
{
	"_id" : ObjectId("5e818d555b72b98071a78814"),
	"user" : "user2",
	"name" : "omaetachi",
	"status" : "guest"
}
```
##menampilkan data secara spesifik
> db.data.find({user:"user1"}).pretty()
```
{
	"_id" : ObjectId("5e818d555b72b98071a78813"),
	"user" : "user1",
	"name" : "watashi",
	"status" : "admin"
}
```