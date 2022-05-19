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
<?php /**PATH /opt/lampp/htdocs/chartman/Flowchart/resources/views/layouts/head.blade.php ENDPATH**/ ?>