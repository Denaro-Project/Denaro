<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ImageController extends Controller
{
    public function upload(Request $request)
    {
        $request->validate([
            'imageFile' => 'required|image|max:2048', // Max 2MB
        ]);

        // use the same name as validated field
        $path = $request->file('imageFile')->store('images', 'public');
        
        // Save to database if needed
        // ImageDirectory::create(['path' => $path, 'filename' => basename($path)]);

        return back()->with('success', 'Image uploaded successfully')->with('path', $path);
    }
}
