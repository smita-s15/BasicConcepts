# AWS 1-Week Learning Pathway

A focused beginner-friendly plan to start learning AWS in one week.

---

## Day 1 – Orientation & Fundamentals

**Goal:** Understand AWS basics and set up your account.

- Create an [AWS Free Tier account](https://aws.amazon.com/free)
- Learn AWS fundamentals:
  - Regions & Availability Zones
  - Core services: EC2 (compute), S3 (storage), RDS (databases), IAM (security)
- Watch: AWS Cloud Practitioner Essentials (first 2 modules) on [AWS Skill Builder](https://explore.skillbuilder.aws/)
- Hands-on:
  - Set up MFA (Multi-Factor Authentication) in IAM
  - Explore the AWS Management Console

---

## Day 2 – Compute: EC2

**Goal:** Launch and manage virtual servers.

- Understand EC2 concepts (instances, AMIs, instance types, pricing)
- Hands-on:
  - Launch an EC2 instance (Amazon Linux 2)
  - SSH into it and install Nginx
  - Stop, start, and terminate the instance
- Learn Security Groups basics (firewall rules)

---

## Day 3 – Storage: S3

**Goal:** Learn cloud storage and permissions.

- Understand S3 buckets, objects, and storage classes
- Hands-on:
  - Create an S3 bucket
  - Upload/download files via Console & CLI
  - Set up bucket policies for public access (and remove them)
- Explore Lifecycle rules for data management

---

## Day 4 – Databases: RDS

**Goal:** Deploy a managed database.

- Understand RDS basics (MySQL/PostgreSQL on AWS)
- Hands-on:
  - Launch an RDS MySQL instance
  - Connect using a SQL client
  - Create a table and insert data
- Learn cost-saving tips for RDS in Free Tier

---

## Day 5 – IAM & Permissions

**Goal:** Manage security in AWS.

- Learn IAM users, groups, roles, and policies
- Hands-on:
  - Create an IAM user with console and CLI access
  - Attach policies (e.g., AmazonS3ReadOnlyAccess)
  - Test permissions by logging in as that user

---

## Day 6 – Networking & Deployment

**Goal:** Understand VPC basics and deploy a simple app.

- Learn VPC, subnets, Internet Gateways, route tables
- Hands-on:
  - Create a VPC with a public subnet
  - Launch EC2 in that subnet
  - Deploy a small app (Node.js / Python Flask)

---

## Day 7 – Wrap-Up Project

**Goal:** Bring it all together.

- Mini Project:
  1. EC2 instance running your app
  2. Static files hosted on S3
  3. Database on RDS
  4. IAM roles controlling access
- Document your steps
- Explore AWS CLI for automation

---

## Extra Tips

- Use [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) for best practices
- Keep AWS billing alerts ON
- Monitor [AWS Free Tier Usage Alerts](https://aws.amazon.com/free/free-tier-faqs/#monitor-your-free-tier-usage)
- Join the AWS re/Start community for peer learning

---

**Happy Learning!**
