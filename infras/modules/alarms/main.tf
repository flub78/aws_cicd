
resource "aws_cloudwatch_metric_alarm" "low_cpu_alarm" {
  alarm_name          = "TF_Low_CPU_Alarm"
  comparison_operator = "LessThanThreshold"
  evaluation_periods  = "6"
  metric_name         = "CPUUtilization"
  namespace           = "AWS/EC2"
  period              = "300"
  statistic           = "Average"
  threshold           = "2"
  alarm_description   = "This metric monitor low CPU utilization for an hour and shuts down the instance if it remains below 2%."
  dimensions = {
    InstanceId = var.instance_id
  }

  alarm_actions = [
    "arn:aws:automate:eu-west-3:ec2:stop",
  ]
}
