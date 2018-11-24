<?php

require 's3.php';

$s3 = new S3('[key_provided_by_AWS_S3]', '[private_key_provided_by_AWS_S3]');


$new_name = time() . '.txt';

S3::putObject(
	$s3->inputFile('[text_file_saved_in_phplocalhost_path', false),
	'[S3_bucket_name]',
	$new_name,
	S3::ACL_PUBLIC_READ,
	array(),
	array(),
	S3::STORAGE_CLASS_RRS
);
