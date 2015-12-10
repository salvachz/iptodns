<?php
require_once('header.php');
?>
        <div id="search-box">
            <form action="search.php" method="GET">
                <input type="text" name="ip" values="" placeholder="192.168.0.1"/>
                <input type="submit" value="search" />
            </form>
        </div><!--search-box-->
<?php
require_once('footer.php');
?>
