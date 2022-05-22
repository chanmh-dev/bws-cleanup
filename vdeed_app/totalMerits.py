from vdeed_app.forms import plasticForm, sutraRecitationForm, mantraRecitationForm
from vdeed_app.models import plastic, paper, misc
from django.db.models import Sum


def total_plastic(context):
    new_plastic_bag_counter = 0
    new_plastic_bottle_counter = 0
    new_plastic_cup_straw_counter = 0
    new_plastic_wrapper_counter = 0
    form_plastic = plasticForm()
    all_plastic = plastic.objects.all()
    #print('all_plastic', all_plastic)
    if (all_plastic):
        new_plastic_bag_counter = plastic.objects.aggregate(
            Sum('plastic_bag_counter'))['plastic_bag_counter__sum']
        new_plastic_bottle_counter = plastic.objects.aggregate(
            Sum('plastic_bottle_counter'))['plastic_bottle_counter__sum']
        new_plastic_wrapper_counter = plastic.objects.aggregate(Sum('plastic_wrapper_counter'))[
            'plastic_wrapper_counter__sum']
        new_plastic_cup_straw_counter = plastic.objects.aggregate(
            Sum('plastic_cup_straw_counter'))['plastic_cup_straw_counter__sum']

    context['form_plastic'] = form_plastic
    print('plastic_bag_counter', new_plastic_bag_counter)
    context['plastic_bag_counter'] = new_plastic_bag_counter
    context['plastic_bottle_counter'] = new_plastic_bottle_counter
    context['plastic_wrapper_counter'] = new_plastic_wrapper_counter
    context['plastic_cup_straw_counter'] = new_plastic_cup_straw_counter


def total_sutra(context):
    new_paper_tissue_counter = 0
    new_paper_counter = 0
    new_paper_cup_counter = 0
    new_paper_cigarette_butt_counter = 0
    form_paper = sutraRecitationForm()
    all_paper = paper.objects.all()
    #print('all_paper', all_paper)
    if (all_paper):
        new_paper_tissue_counter = paper.objects.aggregate(
            Sum('paper_tissue_counter'))['paper_tissue_counter__sum']
        new_paper_counter = paper.objects.aggregate(
            Sum('paper_counter'))['paper_counter__sum']
        new_paper_cup_counter = paper.objects.aggregate(Sum('paper_cup_counter'))[
            'paper_cup_counter__sum']
        new_paper_cigarette_butt_counter = paper.objects.aggregate(
            Sum('paper_cigarette_butt_counter'))['paper_cigarette_butt_counter__sum']

    context['form_paper'] = form_paper
    context['paper_tissue_counter'] = new_paper_tissue_counter
    context['paper_counter'] = new_paper_counter
    context['paper_cup_counter'] = new_paper_cup_counter
    context['paper_cigarette_butt_counter'] = new_paper_cigarette_butt_counter


def total_mantra(context):
    new_misc_glass_bottle_counter = 0
    new_misc_mask_counter = 0
    new_misc_others_counter = 0
    new_misc_can_counter = 0
    form_misc = mantraRecitationForm()
    all_misc = misc.objects.all()
    #print('all_misc', all_misc)
    if (all_misc):
        new_misc_glass_bottle_counter = misc.objects.aggregate(
            Sum('misc_glass_bottle_counter'))['misc_glass_bottle_counter__sum']
        new_misc_mask_counter = misc.objects.aggregate(
            Sum('misc_mask_counter'))['misc_mask_counter__sum']
        new_misc_others_counter = misc.objects.aggregate(Sum('misc_others_counter'))[
            'misc_others_counter__sum']
        new_misc_can_counter = misc.objects.aggregate(
            Sum('misc_can_counter'))['misc_can_counter__sum']

    context['form_misc'] = form_misc
    context['misc_glass_bottle_counter'] = new_misc_glass_bottle_counter
    context['misc_mask_counter'] = new_misc_mask_counter
    context['misc_others_counter'] = new_misc_others_counter
    context['misc_can_counter'] = new_misc_can_counter
