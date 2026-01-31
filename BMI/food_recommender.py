def recommend_food(category):
    food = {
        "Underweight": [
            "Lean proteins (eggs, chicken, fish, tofu)",
            "Whole grains (brown rice, oats, quinoa)",
            "Healthy fats (nuts, seeds, olive oil, avocado)",
            "Dairy or dairy alternatives (yogurt, milk, fortified plant milks)",
            "Fatty fish (salmon, sardines)",
            "Calorie-dense snacks (nut butter, trail mix, seeds)",
            "Stay hydrated (water, coconut water)"
        ],

        "Normal": [
            "Balanced meals (protein + carbs + healthy fats)",
            "Fruits and vegetables (variety of colours)",
            "Whole grains",
            "Lean protein sources",
            "Dairy or dairy alternatives",
            "Nuts and seeds",
            "Adequate hydration (water, coconut water)"
        ],

        "Overweight": [
            "High-fiber vegetables",
            "Lean proteins",
            "Low added sugar foods",
            "Portion control",
            "Resistant starches (lentils, beans, cooled rice/potatoes)",
            "Fruits and legumes",
            "High-protein, blood sugar–balanced meals",
            "Nuts and seeds (in moderation)",
            "Stay hydrated (water, coconut water)"
        ],

        "Obese": [
            "Vegetable-forward meals and snacks",
            "High-fiber foods",
            "Low-calorie, nutrient-dense options",
            "Reduced added sugar intake",
            "Blood sugar–balanced meals",
            "Lean protein sources",
            "Resistant starches",
            "Portion control",
            "Stay hydrated (water, coconut water)"
        ]
    }

    return food.get(category, [])
