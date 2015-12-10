<?php
require_once('header.php');
require_once('lib/Ip.class.php');

$ip_address = addslashes($_REQUEST['ip']);
$ip = new Ip($ip_address);

if($ip->is_valid()){
?>



<?php
$domains = $ip->get_domains();
    if(sizeof($domains)){ ?>
<ul id="dns-list">
<?php
        foreach($domains as $domain){
?>
    <li>
      <a target="_blank" href="http://<?=$domain?>"><?=$domain?></a>
      <img label="favicon" src="http://<?=$domain?>/favicon.ico" />
    </li>
<?php 
        } ?>
</ul>
<?php
    }else{ /*if there not domains to this ip*/
?>
<div id="msg-invalid">
    <span>We could not find any DNS for that IP address</span>
    <span style="display:block;font-size:4em"> ''/</span>
</div>
<?php
    }
}else{ /*if is not valid*/?>

<div id="msg-invalid">
<span>Sorry! But this is an invalid IP address</span>
<span style="display:block;font-size:4em"> ''/</span>
</div>
<?php
}
require_once('footer.php');
?>
