from nibabel import nb


nii = nb.load("template.nii.gz")

print(nii.header)
