
var detailed=function (pmcode,date){

   var sql="insert into bms.EF_AP_FEE_DETAIL\n" +
        "select \n" +
        "bms.seq_EF_AP_FEE_DETAIL.nextval,\n" +
        "'"+pmcode+"',\n" +
        "a.ORDER_SOURCE,\n" +
        "to_date('2020-08-14','yyyy-mm-dd'),\n" +
        "a.BUSINESS_TYPE,\n" +
        "a.FEE_CODE,\n" +
        "a.FEE_LINE_NO,\n" +
        "a.FEE_SOURCE_NO,\n" +
        "a.COMBIN_LINE_NO,\n" +
        "a.ORDER_TYPE,\n" +                                    //a.ORDER_TYPE   业务小类
        "a.FEE_ORDER_TYPE,\n" +                                //a.FEE_ORDER_TYPE  业务大类
        "a.CLEARING_CUSTOMER_CODE,\n" +
        "a.CLEARING_SUPPLIER_CODE,\n" +                                      //a.CLEARING_SUPPLIER_CODE   供应商编码
        "a.WH_CODE,\n" +
        "a.SKU_LINE_NO,\n" +
        "a.SKU_CODE,\n" +
        "a.BULK,\n" +
        "a.GROSS_WEIGHT,\n" +
        "a.ETCD_WEIGHT,\n" +
        "a.QUANTITY,\n" +
        "a.PRICE,\n" +
        "a.SKU_STATUS,\n" +
        "a.LINE_CODE,\n" +
        "a.SKU_AGE,\n" +
        "a.BUBBLE_WEIGHT,\n" +
        "a.OWNER_CODE,\n" +
        "a.AMOUNT,\n" +
        "a.TAX_RATE,\n" +
        "a.TAX_AMOUNT,\n" +
        "a.NO_TAX_AMOUNT,\n" +
        "a.CURRENCY,\n" +
        "a.CURRENCY_RATE,\n" +
        "a.OILCARD_PAY_RATIO,\n" +
        "a.OILCARD_PAY_AMOUNT,\n" +
        "a.IS_ALREADY_APPORTION,\n" +
        "'',\n" +
        "'',\n" +
        "a.MATCH_NO,\n" +
        "a.COST_JOB_ID,\n" +
        "a.CMP_COST_JOB_ID,\n" +
        "a.COMPARISON_JOB_ID,\n" +
        "a.CONTRACT_NO,\n" +
        "a.OIL_RATIO,\n" +
        "a.CHANGEBILLID,\n" +
        "a.OILCARD_PREPAY_AMOUNT,\n" +
        "a.VIRTUAL_FLAG,\n" +
        "a.BUSINESS_ORDER_TYPE,\n" +
        "a.ORDER_LOGISTIC_TYPE,\n" +
        "a.LOADING_TYPE,\n" +
        "a.C_NODE,\n" +
        "a.SOURCE_FROM,\n" +
        "20,\n" +
        "a.CONFIRM_STATUS,\n" +
        "a.REMARK,\n" +
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
        "a.PRECALCULATE,\n" +
        "1,\n" +
        "'HC0066728',\n" +
        "a.SOURCE_CUSTOMER_CODE,\n" +
        "0,\n" +
        "'',\n" +
        "0\n" +
        "from bms.ef_ap_fee_detail a where a.head_pm_code in (\n" +
        "select b.pm_code from bms.ef_ap_fee_header b where b.supplier_code_settlement='HC0060881' and b.order_no in (\n" +
        "'"+date+"'\n" +
        "));"


    return sql

}




exports.detailed=detailed
