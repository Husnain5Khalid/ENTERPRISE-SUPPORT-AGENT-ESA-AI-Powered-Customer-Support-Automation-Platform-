# Account Verification Procedure

**Document Version:** 1.0
**Department:** Identity & Access Management
**Owner:** Security Operations Team
**Last Updated:** 2026-07-20

---

# Purpose

This document defines the standard procedure for verifying a customer's identity before performing account-related actions.

---

# Scope

Applicable to all customer accounts requesting sensitive operations such as password resets, SIM replacement, subscription changes, or account updates.

---

# Business Rules

- Customer identity must always be verified before performing sensitive actions.
- Verification must use the customer's registered contact information.
- Verification attempts are limited to three failures.
- AI must never bypass the verification process.

---

# Standard Operating Procedure (SOP)

## Step 1 – Request Customer ID

Ask the customer for:

- Customer ID
- Registered mobile number or email address

---

## Step 2 – Verify Information

Confirm that the provided information matches the customer record.

---

## Step 3 – OTP Verification

Send a One-Time Password (OTP) to the registered mobile number or email.

- OTP validity: 5 minutes
- Maximum attempts: 3

---

## Step 4 – Complete Verification

If the OTP is successfully validated, continue with the requested service.

---

# Exceptions

- Business accounts require manual verification.
- Customers reporting account compromise must not continue with self-service verification.

---

# Escalation Criteria

Escalate immediately if:

- Customer fails verification three times.
- Customer reports unauthorized account access.
- Registered contact information cannot be verified.
- Fraud indicators are detected.

---

# References

Identity Verification Policy v3.1
Security Operations Manual