var myheadsql = function(numbers) {


    var sql = "insert into ef_ap_fee_header\n" +
        "select \n" +
        "bms.seq_EF_AP_FEE_HEADER.nextval+1,\n" +
        "sys_guid()||'-'||rownum,\n" +
        "a.CUSTOMER_NO,\n" +
        "a.ORDER_NO,\n" +
        "a.ETDO_NO,\n" +
        "a.ANNTO_ORDER_NO,\n" +
        "a.CUSTOMER_CODE,\n" +
        "a.SUPPLIER_CODE,\n" +
        "a.BURSAR_BODY,\n" +
        "a.COMPANY_CODE,\n" +
        "a.SITE_CODE,\n" +
        "a.BULK,\n" +
        "a.GROSS_WEIGHT,\n" +
        "a.ETCD_WEIGHT,\n" +
        "a.QUANTITY,\n" +
        "a.REMARK,\n" +
        "a.EMPTY_FLAG,\n" +
        "a.REC_VER,\n" +
        "a.REC_STATUS,\n" +
        "a.CREATOR,\n" +
        "sysdate,\n" +
        "a.MODIFIER,\n" +
        "sysdate,\n" +
        "a.SUB_STR1,\n" +
        "a.SUB_STR2,\n" +
        "a.SUB_STR3,\n" +
        "a.SUB_STR4,\n" +
        "a.SUB_NUM1,\n" +
        "a.SUB_NUM2,\n" +
        "a.SUB_NUM3,\n" +
        "a.SUB_NUM4,\n" +
        "a.SUB_DATE1,\n" +
        "a.SUB_DATE2,\n" +
        "a.SUB_DATE3,\n" +
        "a.SUB_DATE4,\n" +
        "1,\n" +
        "'HC0066728',\n" +
        "a.ETTA_ORDER_DATE,\n" +
        "a.FROM_ADDRESS_NAME,\n" +
        "a.TO_ADDRESS_NAME,\n" +
        "a.ETTA_RATE_MILEAGE,\n" +
        "a.ETTA_CONTRACT_NO,\n" +
        "a.SOURCE_JOB_ID\n" +
        "from bms.ef_ap_fee_header a where a.supplier_code_settlement='HC0060881' and a.order_no in (\n" +
        "'" + numbers + "'\n" +
        ");\n";


    return sql

};


exports.myheadsql = myheadsql;