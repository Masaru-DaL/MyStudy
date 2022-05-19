<!doctype html>
<html lang="ja">
<head>

    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <?php if(isset($title)): ?>
    <title><?php echo e($title); ?> - -- chartman --></title>
    <?php else: ?>
    <title>-- chartman --></title>
    <?php endif; ?>

    <link rel="stylesheet" href="<?php echo e(asset('css/style.css')); ?>">

</head>
<body>

<header>
        <div class="header_left_btn">
            <a href="" class="btn header_left">user</a>
        </div>
        <div class="header__center_btn">
            <nav>
                <ul class="header_ul">
                    <div class="header_li_left">
                        <li class="header_li"><a href="" class="header_link">■</a></li>
                        <li class="header_li"><a href="" class="header_link">(…)</a></li>
                        <li class="header_li"><a href="" class="header_link">虫眼鏡</a></li>
                    </div>
                    <div class="header_li_right">
                        <li class="header_li"><a href="" class="header_link">手</a></li>
                        <li class="header_li"><a href="" class="header_link">雲</a></li>
                        <li class="header_li"><a href="" class="header_link">？</a></li>
                    </div>
                </ul>
            </nav>

        </div>
        <div class="header_right_btn">
            <a href="" class="btn header_right">share</a>
        </div>

</header>


<div class="flowchart_page">
    <div class="container">
        <div class="sidebar_left">
        </div>
        <div class="main">
        </div>
        <div class="sidebar_right">
        </div>
    </div>
</div>
</body>
<?php /**PATH /opt/lampp/htdocs/chartman/Flowchart/resources/views/flowchart.blade.php ENDPATH**/ ?>