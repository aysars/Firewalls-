import random

def generate_random_ip():
    return f"192.168.1.{random.randint(1,20)}"

def check_firewall_rules(ip,rules):
    for rule_ip,action in rules.items():
       if ip == rule_ip:
        return action
    return "allow"     

def main():
   firewall_rules = {
        "192.168.1.2": "block",
        "192.168.1.7": "block",
        "192.168.1.12": "block",
        "192.168.1.13": "block",
        "192.168.1.5": "block",
        "192.168.1.14": "block"
    } 
   \for _ in range(20):
    ip_address= generate_random_ip()
    action = check_firewall_rules(ip_address, firewall_rules )
    random_number = random.randint(0,9999)
    print(f"IP:{ip_address}, Action{action}, Random number{random_number}")




if __name__ == "__main__":
    main()