from django import template

register = template.Library()

@register.filter(name="job")
def job(value, arg):
    if arg != "abb":
        if value == "K":
            return "Kindergarten Teacher"
        if value == "1":
            return "1st Grade Teacher"
        if value == "2":
            return "2nd Grade Teacher"
        if value == "3":
            return "3rd Grade Teacher"
        if value == "4":
            return "4th Grade Teacher"
        if value == "5":
            return "5th Grade Teacher"
        if value == "6":
            return "6th Grade Teacher"
    else:
        if value == "K":
            return "Kindergarten"
        if value == "1":
            return "First Grade"
        if value == "2":
            return "Second Grade"
        if value == "3":
            return "Third Grade"
        if value == "4":
            return "Fourth Grade"
        if value == "5":
            return "Fifth Grade"
        if value == "6":
            return "Sixth Grade"
