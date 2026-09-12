import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_messy_dataset(num_rows=10000, output_file='data/tasks.csv'):
    np.random.seed(42)
    random.seed(42)

    # Base features
    base_date = datetime.now()
    
    data = []
    
    task_types = ["Development", "Testing", "Design", "Documentation", "Other"]
    messy_task_types = ["development", "DEV", "Testing ", "  Design", "doc", "Other", None]

    for i in range(1, num_rows + 1):
        # Introduce duplicate randomly
        if random.random() < 0.02 and len(data) > 0:
            row = data[-1].copy()
            data.append(row)
            continue
            
        created_date = base_date - timedelta(days=random.randint(0, 365))
        
        # Timeline errors (deadline before created)
        if random.random() < 0.05:
            deadline_date = created_date - timedelta(days=random.randint(1, 10))
        else:
            deadline_date = created_date + timedelta(days=random.randint(1, 60))
            
        # Effort with missing and outliers
        effort_rand = random.random()
        if effort_rand < 0.05:
            estimated_effort = np.nan
        elif effort_rand < 0.10:
            estimated_effort = round(random.uniform(200, 999), 1) # Outlier
        else:
            estimated_effort = round(random.uniform(0.5, 40.0), 1)
            
        # Impact with missing and invalid
        impact_rand = random.random()
        if impact_rand < 0.05:
            business_impact = np.nan
        elif impact_rand < 0.10:
            business_impact = random.choice([-1, 0, 11, 15]) # Invalid
        else:
            business_impact = random.randint(1, 10)
            
        # Urgency with invalid
        urgency_rand = random.random()
        if urgency_rand < 0.05:
            urgency = random.choice([0, 12, 100]) # Invalid
        else:
            urgency = random.randint(1, 10)
            
        # Dependencies with negative
        dep_rand = random.random()
        if dep_rand < 0.05:
            dependency_count = random.randint(-5, -1)
        else:
            dependency_count = random.randint(0, 10)
            
        # Task type with messiness
        if random.random() < 0.15:
            task_type = random.choice(messy_task_types)
        else:
            task_type = random.choice(task_types)
            
        # Generate target loosely based on rules so there is some pattern
        # The ML team will have to clean it to get perfect logic
        row = {
            "task_id": i,
            "created_date": created_date.strftime("%Y-%m-%d"),
            "deadline_date": deadline_date.strftime("%Y-%m-%d"),
            "estimated_effort": estimated_effort,
            "business_impact": business_impact,
            "urgency": urgency,
            "dependency_count": dependency_count,
            "task_type": task_type,
            # We won't generate the priority_label perfectly, we'll let it be missing 
            # for 10% to force them to use the logic to label it, or we label it loosely.
            # Let's generate a naive label.
            "priority_label": random.choice(["Low", "Medium", "High", "Critical"]) if random.random() < 0.1 else None
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    
    # We will compute a somewhat realistic priority label for the ones not randomly set
    def apply_naive_score(row):
        if pd.notna(row['priority_label']): return row['priority_label']
        try:
            score = (float(row['business_impact']) * 4) + (float(row['urgency']) * 3) + (float(row['dependency_count']) * 2)
            if score >= 80: return "Critical"
            if score >= 60: return "High"
            if score >= 40: return "Medium"
            return "Low"
        except:
            return "Medium" # Fallback for nan
            
    df['priority_label'] = df.apply(apply_naive_score, axis=1)
    
    df.to_csv(output_file, index=False)
    print(f"Generated {len(df)} rows in {output_file}")

if __name__ == "__main__":
    generate_messy_dataset()
