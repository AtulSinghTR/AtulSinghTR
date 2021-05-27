mkdir -p outdir/
> outdir/all_sqs.txt

for x in {{a..z},{A..Z}}
do
    echo -n "$x, "
    aws sqs list-queues  --queue-name-prefix "$x"  | grep http >> all_sqs.txt
done