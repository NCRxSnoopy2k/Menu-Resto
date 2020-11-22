from json import dump

file_path = "mytxt/menu.json"
mode = "w"

menus = {
	"20200905-R001P100" : {
		"nama" : "Pecel lele",
		"harga" : "10000",
		"stok" : "80",

	},
	"20200907-R002A100" : {
		"nama" : "Ayam goreng",
		"harga" : "10000",
		"stok" : "80",

	}
}

with open(file_path, mode) as file:
	dump(menus, file)