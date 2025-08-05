def print_banner():
      print("🌱 Welcome to EcoCal🌱 By Stesha Simon")
      print("Answer the following questions to find out your ecological footprint and learn how you can live more sustainably.\n")

  def calculate_footprint():
      score = 0

      print("1. How often do you use a car?")
      print("a) Never\nb) Occasionally\nc) Frequently\nd) Daily")
      answer = input("Your answer: ").strip().lower()
      if answer == 'a':
          score += 1
      elif answer == 'b':
          score += 3
      elif answer == 'c':
          score += 5
      elif answer == 'd':
          score += 7
      print("\n🚗 Fun Fact: Transportation is one of the largest sources of greenhouse gas emissions globally. Choosing public transport or biking can significantly reduce your carbon footprint.\n")

      print("2. What best describes your diet?")
      print("a) Vegan\nb) Vegetarian\nc) Occasional meat\nd) Regular meat")
      answer = input("Your answer: ").strip().lower()
      if answer == 'a':
          score += 1
      elif answer == 'b':
          score += 3
      elif answer == 'c':
          score += 5
      elif answer == 'd':
          score += 7
      print("\n🥗 Fun Fact: Producing meat requires significantly more resources and generates more greenhouse gases than plant-based foods. Reducing meat consumption can lower your ecological footprint.\n")

      print("3. How energy-efficient is your home?")
      print("a) Very efficient (solar panels, energy-saving appliances)\nb) Moderately efficient (some energy-saving measures)\nc) Slightly efficient (few energy-saving measures)\nd) Not efficient at all")
      answer = input("Your answer: ").strip().lower()
      if answer == 'a':
          score += 1
      elif answer == 'b':
          score += 3
      elif answer == 'c':
          score += 5
      elif answer == 'd':
          score += 7
      print("\n💡 Fun Fact: Energy-efficient homes use less energy to perform the same tasks, which helps reduce greenhouse gas emissions and save money on utility bills.\n")

      print("4. How much waste do you produce?")
      print("a) Very little (recycle/compost most waste)\nb) Moderate (recycle/compost some waste)\nc) High (recycle/compost occasionally)\nd) Very high (rarely recycle/compost)")
      answer = input("Your answer: ").strip().lower()
      if answer == 'a':
          score += 1
      elif answer == 'b':
          score += 3
      elif answer == 'c':
          score += 5
      elif answer == 'd':
          score += 7
      print("\n♻️ Fun Fact: Recycling and composting can significantly reduce the amount of waste that ends up in landfills. Landfills are major sources of methane, a potent greenhouse gas.\n")

      return score

  def display_results(score):
      print("\nYour Ecological Footprint Score: ", score)
      if score <= 10:
          print("🌟 Excellent! You have a very low ecological footprint. Keep up the great work!")
      elif score <= 20:
          print("👍 Good job! You have a moderate ecological footprint. There are still areas where you can improve.")
      elif score <= 30:
          print("⚠️ Your ecological footprint is quite high. Consider making more sustainable choices.")
      else:
          print("🚨 Your ecological footprint is very high. It's important to make significant changes to reduce your impact on the environment.")

  def main():
      print_banner()
      score = calculate_footprint()
      display_results(score)

  if __name__ == "__main__":
      main()
  