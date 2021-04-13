let data = require("./export/out.json");

var fs = require("fs");
var util = require("util");
var log_file = fs.createWriteStream(__dirname + "/export/out.csv", { flags: "w" });
var log_stdout = process.stdout;

console.log = function (d) {
  //
  log_file.write(util.format(d) + "\n");
  log_stdout.write(util.format(d) + "\n");
};
console.log("Category,Account,Value,Description,Date");
for (let i = 0; i < data.length; i++) {
  console.log(data[i].Categoria + "," + data[i].Conta + "," + data[i].Valor + "," + data[i].Descricao + "," + data[i].Data);
}
