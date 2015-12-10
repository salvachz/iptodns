<?php

class Ip{

    public $address;

    function Ip($address){
        $this->address = $address;
        $this->mysql = mysql_connect('127.0.0.1','root','');
        mysql_select_db('iptodns', $this->mysql);
    }

    function is_valid(){
        $parts = explode(".",$this->address);
        if(sizeof($parts)!=4)
            return false;
        foreach($parts as $part){
            if(!is_numeric($part))
                return false;
            if(strlen($part)>3)
                return false;
        }

        return true;
    }

    function get_domains(){
        $qry = "SELECT dnsName FROM DnsIp JOIN Dns ON DnsId = dipDnsId WHERE dipIp = INET_ATON('".$this->address."')";
        $result = Array();
        $qry = mysql_query($qry,$this->mysql);
        echo mysql_error();
        while($row = mysql_fetch_row($qry)){
            $result[] = $row[0];
        }
        return $result;
    }
}

?>
