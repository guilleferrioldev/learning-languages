import type { Metadata } from "next";
import '@/app/ui/global.css';
import {  montserrat } from '@/app/ui/fonts';

export const metadata: Metadata = {
  title: "Learning Next",
  description: "Learning Next",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${montserrat.className} antialiased`}>
        {children}
        <footer className='py-10 flex justify-center items-center'>
          Hecho con 🧡 por la gente de Vercel
          </footer>
        </body>    
    </html>
  );
}
