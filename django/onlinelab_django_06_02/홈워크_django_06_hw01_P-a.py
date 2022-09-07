def update(request,pk):
    reservation = Reservation.objects.get(pk)
    if request.method == "POST":
        # __(a)__
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles:detail",reservation.pk)
    else:
        # __(b)__
        form = AuthenticationForm()
    context = {
        'reservation':reservation,
        'form':form,
    }
    return render(request,"articles/update.html",context)