from collections import namedtuple

Rule = namedtuple("Rule", "a b")


def puzzle1(filename: str):
  rules, updates = read_file(filename)
  total = 0

  for update in updates:
    if not is_update_invalid(update, rules):
      total += update[len(update) // 2]

  return total


def puzzle2(filename: str):
  rules, updates = read_file(filename)
  total = 0

  for update in updates:
    if is_update_invalid(update, rules):
      # Continuously move around pages in the update until all rules match
      while is_update_invalid(update, rules):
        move_item_per_rule(update, rules)

      total += update[len(update) // 2]

  return total


def move_item_per_rule(update, rules):
  for rule in rules:
    for index, page in enumerate(update):
      before = update[0:index]
      after = update[index + 1:len(update)]

      if page == rule.a and rule.b in before:
        raise Exception("Never happens, apparently")

      if page == rule.b and rule.a in after:
        update.remove(page)
        i = update.index(rule.a)
        update.insert(i + 1, page)
        return


def is_update_invalid(update, rules):
  invalid = False

  for index, page in enumerate(update):
    if invalid:
      break

    before = update[0:index]
    after = update[index + 1:len(update)]

    for rule in rules:
      if page == rule.a and rule.b in before:
        invalid = True
        break
      if page == rule.b and rule.a in after:
        invalid = True
        break

  return invalid


def read_file(filename):
  rules = []
  updates = []

  with open(filename, "r") as file:
    for line in file:
      if "|" in line:
        rule = [int(page.strip()) for page in line.split("|")]
        rules.append(Rule(*rule))

      if "," in line:
        updates.append([int(page.strip()) for page in line.split(",")])

  return rules, updates
