const db = require('./oracledb');
const head = require('./head');
const detailed = require('./detailed');
const fs = require('fs');
const  dele=require('./delete')
const  path=require('path')




var array = fs.readFileSync(path.join(__dirname,'date.txt')).toString().split("\r\n");




function add_detailed(sql) {
    db.query(sql, function(res) {
        res.forEach(function(itme, index) {
            var arr = detailed.detailed(itme.PM_CODE, itme.ORDER_NO);
            let fd = fs.openSync(path.join(__dirname,'detailed.sql'), 'a');
            fs.open(path.join(__dirname,'detailed.sql'), 'a', function(err, fd) {
                if (err) {
                    console.log(err)
                } else {
                    fs.writeFile(fd, arr + '\n', (err) => {
                        if (err) {
                            console.log(err)
                        }

                        fs.close(fd, (err) => {
                            if (err) {
                                console.log(err)
                            }
                        })
                    });
                }
            });

        });
    })


    console.log('写入成功');
}



function add_head() {
    array.forEach(function(itme) {
        var arr = head.myheadsql(itme);
        let fd = fs.openSync(path.join(__dirname,'head.sql'), 'w');
        fs.open(path.join(__dirname,'head.sql'), 'a', function(err, fd) {
            if (err) {
                console.log(err)
            } else {
                fs.writeFile(fd, arr + '\n', (err) => {
                    if (err) throw err;
                    fs.close(fd, (err) => {
                        if (err) {
                            console.log(err)
                        }
                    })
                });
            }
        });
    });

    console.log('写入成功');
}




function add() {
    fs.writeFile('./mytest/detailed.sql', '', function(err) { if (err) return err })
    array.forEach(function(itme) {
        var sql = "select a.pm_code,a.order_no from ef_ap_fee_header a where a.order_no in (\n" +
            "'" + itme + "'\n" +
            ") and  a.is_replace_settlement=1 and a.supplier_code_settlement='HC0066728'"

        add_detailed(sql)
        // dele.arheader(itme)
        // dele.ardetail(itme)
        // dele.apheader(itme)
        // dele.apdetail(itme)

    })
}



function delete_sql1(){
    array.forEach(function (itme){
        dele.apfee_detail(itme)
        dele.arfee_detail(itme)
    })
}



function delete_sql2(){
    array.forEach(function (itme){
        dele.apfee_header(itme)
        dele.arfee_header(itme)
    })
}






console.log(array)








