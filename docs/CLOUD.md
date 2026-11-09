# Cloud plan

Owner: ........   Cloud provider: ........ (the course uses Google Cloud; another one is fine)

You don't deploy anything: this is the plan you would follow. The S7 curveball is its heart: "Your CTO wants
Popote in the cloud next month with 300 EUR a month. What runs where, what stays off, what is public and what is
private?" Answer it for **your** product.

## Box by box

| Box | Managed service or run by you | Which service | Scale to zero or always on | Public or private | Cost per month |
| --- | --- | --- | --- | --- | --- |
| ........ | | | | | |

For each box: why managed (or not)? What would you lose or gain by doing it yourself?

## The network

- What is the one public front door (a URL, a load balancer)? Who may call it?
- What stays private (internal ingress, private IPs in a VPC)? Who may call each private box (IAM, a service account)?
- Draw it: public on one side, private on the other.

## Scale to zero, cold starts

- Which boxes may sleep when nobody calls them? What does the first customer after a sleep wait?
- Which ones must stay on (minimum one instance), and what does that cost for a whole month?

## The cost

- Every price comes from the provider's own pricing page, with the date you read it. No guess, no blog.
- The total per month, and the biggest line. Does it fit in 300 EUR? If not, what goes, or what changes?
- What stops the bill (a maximum number of instances, a spend cap, a teardown), and what only warns (budget alerts)?

## What we would watch

- The first three numbers on your dashboard the day you go live, and the alert you would set on each.
- What you would do first if the bill doubled.
